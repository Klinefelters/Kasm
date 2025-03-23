from attr import define
from KasmCompiler.functions.base_function import base_function

import logging

@define
class LoadL(base_function):
    
    def __call__(self, line, registers, addresses, values, devices):
        """Load the live value into the register."""
    
        args = line.split("(")[1].strip(")").split(",")

        logging.debug(f"LoadL arguments: {args}")

        reg_a = self.get_register(args[0].strip(), registers)  # Register A (5 bits)
        value = self.get_value(args[1].strip(), values)  # Address (24 bits)

        logging.debug(f"Register A: {reg_a}, Value: {value}")

        binary_instruction = ("010" + reg_a.binary_value[0] + value.binary_value + reg_a.binary_value[1:])
        
        logging.debug(f"LoadL instruction: {binary_instruction}")
        
        hex_instruction = self.binary_to_hex(binary_instruction)
        
        return hex_instruction
        
