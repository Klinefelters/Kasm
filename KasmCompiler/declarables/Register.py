from attr import define

@define
class Register:
    name: str
    binary_value: str

    def __attrs_post_init__(self):
        # Ensure binary_value is in 05b format
        self.binary_value = format(self.binary_value,'05b')

    def __str__(self):
        return f"Register {self.name} = {self.binary_value}"
    
    def __repr__(self):
        return f"Register({self.name}, {self.binary_value})"
    
    def __eq__(self, other):
        return self.name == other.name and self.binary_value == other.binary_value