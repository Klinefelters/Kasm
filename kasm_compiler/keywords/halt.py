from attr import define
from kasm_compiler.keywords.base_keyword import BaseKeyword

@define
class Halt(BaseKeyword):
    name: str = 'Halt'
    operands: list = []