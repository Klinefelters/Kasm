from attr import define
from kasm_compiler.keywords.base_keyword import BaseKeyword
from kasm_compiler.identifiers.register import Register
from kasm_compiler.identifiers.immediate import Immediate

@define
class LoadIL(BaseKeyword):
    keyword: str = 'LOADIL'
    
    def parse(self, args):
        if type(args[0]) is Immediate and type(args[1]) is Register:
            imm = args[0]
            rd = args[1]
        else:
            raise Exception("LOADIL requires an immediate value and a register as arguments")

        return '011' + '00' + imm.parse() + rd.parse()