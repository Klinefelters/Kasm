from attr import define
from kasm_compiler.token import Token

@define
class BaseIdentifier(Token):
    identifier: str = None
    name: str = None
    value: any = None

    def enstantiate(self, name, value):
        self.name=name
        self.value=int(value)
        return self
    
    def parse(self, **kwargs):
        raise NotImplemented