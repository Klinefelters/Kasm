from attr import define
from kasm_compiler.keywords.base_keyword import BaseKeyword
from kasm_compiler.identifiers.device import Device
from kasm_compiler.identifiers.immediate import Immediate

@define
class WIOIH(BaseKeyword):
    """
    WIOIH Imm Da
    write immediate value Imm into device Da as the high byte with low byte set to 0's
    """
    keyword: str = 'WIOIH'
    
    def parse(self, args):
        if type(args[0]) is Immediate and type(args[1]) is Device:
            imm = args[0]
            rd = args[1]
        else:
            raise Exception("WIOIH requires an immediate value and a device as arguments")

        return '110' + '11' + imm.parse() + rd.parse()