from attr import define
from kasm_compiler.keywords.base_keyword import BaseKeyword
from kasm_compiler.identifiers.device import Device
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