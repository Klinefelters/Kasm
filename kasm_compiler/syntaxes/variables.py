from attr import define
from logging import debug, error


@define
class Variable:
    """A class representing a variable in assembly code."""
    name: str = None
    address: int = 0
    line: int = 0

    def load_to_register(self, reg: str) -> str:
        """Load the variable's address into a register."""
        return f"LDL {reg}, {self.address}"