from attr import define
from kasm_compiler.keywords.base_keyword import BaseKeyword

@define
class Halt(BaseKeyword):
    keyword: str = 'HALT'
    
    def parse(self, args):
        return '1111' + '1111' + '1111' + '1111'