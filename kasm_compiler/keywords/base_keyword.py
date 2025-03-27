from attr import define
from kasm_compiler.token import Token

@define
class BaseKeyword(Token):
    keyword: str = None

    def parse(self, args:list) -> str:
        raise NotImplementedError("parse method not implemented")