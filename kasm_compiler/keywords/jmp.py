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
    sel: str = '111'
    
    def parse(self, args):
        if type(args[0]) is Register:
            rb= args[0]
        else:
            raise Exception("JMP requires a register as an argument")

        return '101' + self.sel + '0' + '000' + '000' + rb.parse()
    
@define
class JMPGRT(BaseKeyword):
    """
    JMPGRT [Rb]
    jump the program counter to the value in register Rb if a was greater than b
    """
    keyword: str = 'JMPGRT'
    sel: str = '000'

@define
class JMPEQL(BaseKeyword):
    """
    JMPEQL [Rb]
    jump the program counter to the value in register Rb if a was equal to b
    """
    keyword: str = 'JMPEQL'
    sel: str = '001'

@define
class JMPLST(BaseKeyword):
    """
    JMPLST [Rb]
    jump the program counter to the value in register Rb if a was less than b
    """
    keyword: str = 'JMPLST'
    sel: str = '010'

@define
class JMPUGT(BaseKeyword):
    """
    JMPUGT [Rb]
    jump the program counter to the value in register Rb if unsigned a was greater than unsigned b
    """
    keyword: str = 'JMPUGT'
    sel: str = '011'

@define
class JMPUEQ(BaseKeyword):
    """
    JMPUEQ [Rb]
    jump the program counter to the value in register Rb if unsigned a was equal to unsigned b
    """
    keyword: str = 'JMPUEQ'
    sel: str = '100'

@define
class JMPULT(BaseKeyword):
    """
    JMPULT [Rb]
    jump the program counter to the value in register Rb if unsigned a was less than unsigned b
    """
    keyword: str = 'JMPULT'
    sel: str = '101'