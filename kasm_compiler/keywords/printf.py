from kasm_compiler.keywords.base_keyword import BaseKeyword
from kasm_compiler.identifiers.device import Device
from kasm_compiler.keywords.rwio import WIOIL

from attr import define

@define
class Printf(BaseKeyword):
    """
    PRINTF Str Da
    prints the value at device Da
    """
    keyword: str = 'printf'
    
    def parse(self, args):
        wioil = WIOIL()
        if type(args[1]) is Device:
            rd = args[1]
        else:
            raise Exception("PRINTF requires a device as an argument")
        
        args[0] = args[0].strip('"').strip("'")

        lines = []

        for char in args[0]:
            if ord(char) < 0 or ord(char) > 255:
                raise ValueError(f'Immediate values must be between 0 and 255, got {ord(char)}')
            lines.append(wioil.parse([char, rd]) + '\n')
        
        return ''.join(lines)