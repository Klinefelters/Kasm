from attr import define
from kasm_compiler.identifiers.base_identifier import BaseIdentifier

@define
class Device(BaseIdentifier):
    identifier: str = 'device'

    def parse(self, **kwargs):
        return format(int(self.value), '03b')