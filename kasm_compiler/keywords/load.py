from attr import define
from kasm_compiler.keywords.base_keyword import BaseKeyword
from kasm_compiler.identifiers.register import Register

@define
class Load(BaseKeyword):
    keyword: str = 'LOAD'
    
    def parse(self, args):
        if type(args[0]) is Register and type(args[1]) is Register:
            ra = args[0]
            rd = args[1]
        else:
            raise Exception("LOAD requires two registers as arguments")

        return '010' + '0000' + rd.parse() + ra.parse() + '000'