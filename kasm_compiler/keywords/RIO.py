from attr import define
from kasm_compiler.keywords.base_keyword import BaseKeyword
from kasm_compiler.identifiers.device import Device
from kasm_compiler.identifiers.register import Register

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