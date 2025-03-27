from attr import define
from kasm_compiler.keywords.base_keyword import BaseKeyword

@define
class NoOp(BaseKeyword):
    """
    NOOP
    performs no operation
    """
    keyword: str = 'NOOP'
    
    def parse(self, args):
        return '0000' + '0000' + '0000' + '0000'