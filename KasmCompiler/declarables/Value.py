from attr import define

@define
class Value:
    name: str
    value: int
    ascii_value: chr
    binary_value: str

    def __str__(self):
        return f"Value {self.name} = {self.binary_value}"
    
    def __repr__(self):
        return f"Value({self.name}, {self.binary_value})"
    
    def __eq__(self, other):
        return self.name == other.name and self.binary_value == other.binary_value
    
    @classmethod
    def from_int(cls, name:str, value:int):
        name = name
        binary_value = format(value, '024b')
        if value < 127:
            ascii_value = chr(value)
        else:
            ascii_value = ""
        return cls(name, value, ascii_value, binary_value)
    
    @classmethod
    def from_ascii(cls, name:str, ascii_value:chr):
        name = name
        binary_value = format(ord(ascii_value), '024b')
        value = ord(ascii_value)
        return cls(name, value, ascii_value, binary_value)