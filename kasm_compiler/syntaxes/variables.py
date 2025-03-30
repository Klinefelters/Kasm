from attr import define
from logging import debug, error


@define
class Variable:
    """A class representing a variable in assembly code."""
    name: str = None
    address: int = 0
    low_addr: int = 0
    high_addr: int = 0
    line: int = 0
    next_address: int = 0

    def initialize(self, value: str, line=0) -> None:
        raise NotImplementedError("This method should be implemented by subclasses.")

    def load_to_register(self, reg) -> str:
        """
        Load the variable's address into a register.
        
        THIS USES THE M1 REGISTER AND WILL REPLACE IT'S VALUE
        """
        if self.address in range(0, 0xFF+1):
            return [f"LDRL {reg}, {self.address}"]
        elif self.address in range(0xFF+1, 0xFFFF+1):
            return [
                f"LDRH M1, {self.low_addr}", 
                f"LDRL {reg}, {self.high_addr}", 
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
        orig_address = self.address
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
                instructions.append(f"ADD M0, M0, M1")
                for instruction in self.load_to_register("R0"):
                    instructions.append(instruction)
                instructions.append(f"STR M0, R0")
                
                i += 2
                self.address += 1
            else:
                self.address += 1
                break
        self.next_address = self.address
        self.address = orig_address
        return instructions
    
@define
class Int(Variable):
    """A class representing a variable in assembly code."""
    name: str = ".int"

    def initialize(self, value: str, line=0) -> None:
        value = int(value, 0)

        instructions = []
        for instruction in self.load_to_register("R0"):
            instructions.append(instruction)

        if value in range(0, 0xFF+1):
            instructions.append(f"LDRL M0, {value}")
            instructions.append(f"STR M0, R0")
        elif value in range(0xFF+1, 0xFFFF+1):
            instructions.append(f"LDRL M0, {value & 0x00FF}")
            instructions.append(f"LDRH M1, {value >> 8}")
            instructions.append(f"ADD M0, M0, M1")
            instructions.append(f"STR M0, R0")
            
        else:
            error(f"VALUE ERROR: The value '{value}' on line {self.line} exceeds the maximum value of 65535.")
            exit(1)
        
        return instructions
    

@define
class Label(Variable):
    name: str = ".label"

    def initialize(self, value: str, line=0) -> None:
        value = int(value)+5

        instructions = []
        for instruction in self.load_to_register("M1"):
            instructions.append(instruction)

        if value in range(0, 0xFF+1):
            instructions.append(f"LDRL M0, {value}")
            instructions.append(f"STR M0, M1")
            instructions.append(f"RST M1")
            instructions.append(f"RST M0")
        else:
            error(f"VALUE ERROR: Cannot have more than 255 labels in a single line.")
            exit(1)
        
        return instructions