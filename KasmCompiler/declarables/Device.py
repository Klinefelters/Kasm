from attr import define

@define
class Device:
    name: str
    id_index: int
    binary_value: str

    def __attrs_post_init__(self):
        # Ensure binary_value is in 05b format
        self.binary_value = format(self.id_index,'05b')

    def __str__(self):
        return f"Device {self.name} = {self.binary_value}"
    
    def __repr__(self):
        return f"Device({self.name}, {self.binary_value})"
    
    def __eq__(self, other):
        return self.name == other.name and self.binary_value == other.binary_value
    
    @classmethod
    def from_index(cls, name, index: int):
        print(name)
        print(index)
        name = name
        binary_value = format(index, '05b')
        return cls(name, index, binary_value)