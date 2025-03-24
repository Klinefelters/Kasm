from attr import define
from kasm_compiler.keywords.base_keyword import BaseKeyword

@define
class Halt(BaseKeyword):
    keyword: str = 'Halt'
    
    def parse(self, **kwargs):
        return '1111' + '1111' + '1111' + '1111' + '1111' + '1111' + '1111' + '1111'