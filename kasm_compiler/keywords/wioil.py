from attr import define
from kasm_compiler.keywords.base_keyword import BaseKeyword
from kasm_compiler.identifiers.device import Device
from kasm_compiler.identifiers.immediate import Immediate

@define
class WIOIL(BaseKeyword):
    """
    WIOIL Imm Da
    write immediate value Imm into device Da as the low byte with high byte set to 0's
    """
    keyword: str = 'WIOIL'
    
    def parse(self, args):
        if type(args[0]) is Immediate and type(args[1]) is Device:
            imm = args[0]
            rd = args[1]
        else:
            raise Exception("WIOIL requires an immediate value and a device as arguments")

        return '110' + '10' + imm.parse() + rd.parse()