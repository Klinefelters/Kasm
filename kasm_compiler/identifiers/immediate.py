from attr import define
from kasm_compiler.identifiers.base_identifier import BaseIdentifier

@define
class Immediate(BaseIdentifier):
    identifier: str = 'immediate'

    def enstantiate(self, name, value):
        try:
            value = int(value)
        except ValueError:
            value = ord(value.strip("'").strip('"'))
        value = int(value)
        if value < 0 or value > 255:
            raise ValueError(f'Immediate values must be between 0 and 255, got {value}')
        return super().enstantiate(name, value)

    def parse(self, **kwargs):
        return format(int(self.value), '08b')