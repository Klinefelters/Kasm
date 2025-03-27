from attr import define
from kasm_compiler.identifiers.base_identifier import BaseIdentifier

@define
class Register(BaseIdentifier):
    identifier: str = 'register'

    def parse(self, **kwargs):
        return format(int(self.value), '03b')