from attr import define
from kasm_compiler.keywords.base_keyword import BaseKeyword
from kasm_compiler.identifiers.register import Register
from kasm_compiler.identifiers.immediate import Immediate

@define
class Load(BaseKeyword):
    """
    LOAD Rd [Ra]
    load value from memory at address [Ra] into register Rd
    """
    keyword: str = 'LOAD'
    
    def parse(self, args):
        if type(args[0]) is Register and type(args[1]) is Register:
            ra = args[0]
            rd = args[1]
        else:
            raise Exception("LOAD requires two registers as arguments")

        return '010' + '0000' + rd.parse() + ra.parse() + '000'
    
@define
class LoadIH(BaseKeyword):
    """
    LOADIH Imm Rd
    load immediate value Imm into Rd as the high byte with low byte set to 0's
    """
    keyword: str = 'LOADIH'
    
    def parse(self, args):
        if type(args[0]) is not Immediate and type(args[1]) is Register:
            imm = Immediate().enstantiate(name=None, value=args[0])
            rd = args[1]
        elif type(args[0]) is Immediate and type(args[1]) is Register:
            imm = args[0]
            rd = args[1]
        else:
            raise Exception("LOADIH requires an immediate value and a register as arguments")

        return '011' + '01' + imm.parse() + rd.parse()
    
@define
class LoadIL(BaseKeyword):
    """
    LOADIL Imm Rb
    load immediate value Imm into Rb as the low byte with high byte set to 0's
    """
    keyword: str = 'LOADIL'
    
    def parse(self, args):
        if type(args[0]) is not Immediate and type(args[1]) is Register:
            imm = Immediate().enstantiate(name=None, value=args[0])
            rd = args[1]
        elif type(args[0]) is Immediate and type(args[1]) is Register:
            imm = args[0]
            rd = args[1]
        else:
            raise Exception("LOADIL requires an immediate value and a register as arguments")

        return '011' + '00' + imm.parse() + rd.parse()