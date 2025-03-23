from attr import define
from KasmCompiler.functions.base_function import base_function

import logging

@define
class In(base_function):
    
    def __call__(self, line, registers, addresses, values, devices):
        """Load the live value into the register."""
    
        args = line.split("(")[1].strip(")").split(",")

        logging.debug(f"In arguments: {args}")

        device = self.get_device(args[0].strip(), devices)
        reg_b = self.get_register(args[1].strip(), registers) 

        logging.debug(f"Device: {device}, Register B: {reg_b}")

        binary_instruction = ("1010111000000000000000" + device.binary_value + reg_b.binary_value)
        
        logging.debug(f"In instruction: {binary_instruction}")
        
        hex_instruction = self.binary_to_hex(binary_instruction)
        
        return hex_instruction
        
