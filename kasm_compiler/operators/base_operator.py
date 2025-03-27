from attr import define
from kasm_compiler.token import Token

@define
class BaseOperator(Token):
    name: str = None
    operator: str = None

    def parse(self, **kwargs) -> str:
        raise NotImplementedError("parse method not implemented")