from attr import define
from kasm_compiler.keywords.base_keyword import BaseKeyword
from kasm_compiler.identifiers.register import Register

@define
class Store(BaseKeyword):
    """
    STORE [Ra] Rb
    store value at register Rb into memory at address [Ra]
    """
    keyword: str = 'STORE'
    
    def parse(self, args):
        if type(args[0]) is Register and type(args[1]) is Register:
            ra = args[0]
            rd = args[1]
        else:
            raise Exception("STORE requires two registers as arguments")

        return '100' + '0000' + '000' + ra.parse() + rd.parse()