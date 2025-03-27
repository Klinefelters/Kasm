from attr import define
from kasm_compiler.keywords.base_keyword import BaseKeyword
from kasm_compiler.identifiers.register import Register
from kasm_compiler.identifiers.immediate import Immediate

@define
class LoadIH(BaseKeyword):
    """
    LOADIH Imm Rd
    load immediate value Imm into Rd as the high byte with low byte set to 0's
    """
    keyword: str = 'LOADIH'
    
    def parse(self, args):
        if type(args[0]) is Immediate and type(args[1]) is Register:
            imm = args[0]
            rd = args[1]
        else:
            raise Exception("LOADIH requires an immediate value and a register as arguments")

        return '011' + '01' + imm.parse() + rd.parse()