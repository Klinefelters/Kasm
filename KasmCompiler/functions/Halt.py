from attr import define
from KasmCompiler.functions.base_function import base_function

import logging

@define
class Halt(base_function):
    
    def __call__(self, line, registers, addresses, values, devices):
        """"""
        binary_instruction = (
            "1111" + "1111" + "1111" + "1111" + "1111" + "1111" + "1111" + "1111"
        )
        hex_instruction = self.binary_to_hex(binary_instruction)
        return hex_instruction
        
