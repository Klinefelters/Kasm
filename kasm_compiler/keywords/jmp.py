from attr import define
from kasm_compiler.keywords.base_keyword import BaseKeyword
from kasm_compiler.identifiers.device import Device
from kasm_compiler.identifiers.register import Register

@define
class JMP(BaseKeyword):
    """
    JMP [Rb]
    jump the program counter to the value in register Rb
    """
    keyword: str = 'JMP'
    
    def parse(self, args):
        if type(args[0]) is Register:
            rb= args[0]
        else:
            raise Exception("JMP requires a register as arguments")

        return '101' + '1110' + '000' + '000' + rb.parse()