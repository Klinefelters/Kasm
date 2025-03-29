from attr import define
from logging import debug, error


@define
class Variable:
    """A class representing a variable in assembly code."""
    name: str = None
    address: int = 0
    low_addr: int = 0
    high_addr: int = 0
    next_address: int = 0
    line: int = 0

    def initialize(self, value: str, line=0) -> None:
        raise NotImplementedError("This method should be implemented by subclasses.")

    def load_to_register(self, reg) -> str:
        """Load the variable's address into a register."""
        if self.address in range(0, 0xFF):
            return [f"LDL {reg}, {self.address}"]
        elif self.address in range(0xFF, 0xFFFF):
            return [
                f"LDH M1, {self.low_addr}", 
                f"LDL {reg}, {self.high_addr}", 
                f"ADD {reg}, M1, {reg}",
            ]
    def copy(self):
        """Create a copy of the variable."""
        return self.__class__()

@define
class Ascii(Variable):
    """A class representing a variable in assembly code."""
    name: str = ".ascii"

    def initialize(self, value: str, line=0) -> None:
        self.next_address = self.address
        value = value.strip('"')
        vals = []
        i = 0
        while i < len(value):
            if value[i:i+2] == '\\n':
                vals.append(int(10))
                i += 2
                continue
    
            vals.append(ord(value[i:i+1]))
            i+= 1
        vals.append(0)
        instructions = []
        i = 0
        while i < len(vals):
            if i + 1 < len(vals):
                instructions.append(f"LDRH M0, {vals[i]}")
                instructions.append(f"LDRL M1, {vals[i+1]}")
                instructions.append(f"ADD M1, M0, M1")
                instructions.append(f"LDRL M0, {self.next_address}")
                instructions.append(f"STR M1, M0")
                i += 2
                self.next_address += 1
            else:
                self.next_address += 1
                break
        return instructions