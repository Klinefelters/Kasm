from attr import define
from logging import error, warning

from kasm_compiler.syntaxes.constants import RESERVED_REGISTERS, REGISTER_ALIASES

@define
class Arg:
    value: int = 0
    prefix: str = None
    suffix: str = ''
    cast_type: str = 'int'
    line: int = 0
    bit_size: int = 3 
    optional: list = []

    def __str__(self) -> str:
        """Return a string representation of the argument in binary format."""
        return f"{self.value:0{self.bit_size}b}" 
    
    def _pre_initialize(self, value: str) -> str:
        return value
    
    def _check_value(self) -> None:
        if self.value < 2**(self.bit_size) and self.value >= 0:
            return
        else:
            error(f"VALUE ERROR: The value '{self.value}' on line {self.line} exceeds the maximum value of {2**(self.bit_size)-1} for a {self.bit_size}-bit argument.")
            exit(1)   

    def initialize(self, value: str, line=0) -> None:
        """Initialize the argument with a specific value.

        Args:
            value (int): The integer value to initialize the argument with.
        """
        self.line = line
        value = self._pre_initialize(value)
        if self.prefix is None:
            raise NotImplementedError("Prefix must be defined for this argument type.")
        try:
            if self.prefix != "":
                val = value.split(self.prefix)[1].strip(self.suffix)
            else:
                val = value.strip(self.suffix)
            for v in self.optional:
                val = val.strip(v)
        except IndexError:
            error(f"VALUE ERROR: '{value}' on line {self.line} does not contain the expected prefix '{self.prefix}'.")
            exit(1)
        if self.cast_type == "int":
            self.value = int(val)
        elif self.cast_type == "bin":
            self.value = int(val, 2)
        elif self.cast_type == "hex":
            self.value = int(val, 16)
        elif self.cast_type == "chr":
            if val == '\\n':
                self.value = int(10)
            else:
                self.value = int(ord(val))
        else:
            raise NotImplementedError("Prefix must be defined for this argument type.")
        self._check_value()

@define 
class Literal(Arg):
    bit_size: int = 8
    
    def initialize(self, value, line=0):
        self.line = line 
        if value.startswith("0x"):
            self.prefix = "0x"
            self.cast_type = "hex"
            return super().initialize(value)
        elif value.startswith("0b"):
            self.prefix = "0b"
            self.cast_type = "bin"
            return super().initialize(value)
        elif value.startswith("'") and value.endswith("'"):
            self.prefix = "'"
            self.suffix = "'"
            self.cast_type = "chr"
            return super().initialize(value)
        else:
            self.prefix = ""
            self.cast_type = "int"
            return super().initialize(value)

@define
class Register(Arg):
    prefix: str = "R"
    optional: list = ["[", "]"]

    def _pre_initialize(self, value):
        if value in REGISTER_ALIASES.keys(): 
            return REGISTER_ALIASES[value]
        return super()._pre_initialize(value)
    def _check_value(self):
        if self.value in RESERVED_REGISTERS:
            warning(f"Register R{self.value} on line {self.line} is a reserved register ({RESERVED_REGISTERS[self.value]['Abbr']}: {RESERVED_REGISTERS[self.value]['Full']}).")
        super()._check_value()

@define
class Device(Arg):
    prefix: str = "D"
