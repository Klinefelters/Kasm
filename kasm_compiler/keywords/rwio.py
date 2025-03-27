from attr import define
from kasm_compiler.keywords.base_keyword import BaseKeyword
from kasm_compiler.identifiers.device import Device
from kasm_compiler.identifiers.immediate import Immediate
from kasm_compiler.identifiers.register import Register

@define
class WIO(BaseKeyword):
    """
    WIO Ra Da
    writes the value at register Rb into device Da
    """
    keyword: str = 'WIO'
    
    def parse(self, args):
        if type(args[0]) is Register and type(args[1]) is Device:
            ra = args[0]
            rd = args[1]
        else:
            raise Exception("WIO requires a register and a device as arguments")

        return '110' + '0100' + '000' + ra.parse() + rd.parse()
    
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
    
@define
class RIO(BaseKeyword):
    """
    RIO Rd Da
    reads the value at device Da into register Rd
    """
    keyword: str = 'RIO'
    
    def parse(self, args):
        if type(args[0]) is Register and type(args[1]) is Device:
            ra = args[0]
            rd = args[1]
        else:
            raise Exception("RIO requires a register and a device as arguments")

        return '110' + '0000' + ra.parse() + '000' + rd.parse()