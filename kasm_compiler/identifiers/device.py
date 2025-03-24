from attr import define
from kasm_compiler.identifiers.base_identifier import BaseIdentifier

@define
class Device(BaseIdentifier):
    identifier: str = 'device'