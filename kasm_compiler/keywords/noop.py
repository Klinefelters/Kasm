from attr import define
from kasm_compiler.keywords.base_keyword import BaseKeyword

@define
class NoOp(BaseKeyword):
    keyword: str = 'NOOP'
    
    def parse(self, args):
        return '0000' + '0000' + '0000' + '0000'