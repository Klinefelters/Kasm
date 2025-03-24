from attr import define
from kasm_compiler.identifiers.base_identifier import BaseIdentifier

@define
class Register(BaseIdentifier):
    name: str = ''
    identifier: str = 'register'
    value: int = 0

    def parse(self, **kwargs):
        return format(int(self.value), '05b')