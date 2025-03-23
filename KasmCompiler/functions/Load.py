from attr import define
from KasmCompiler.functions.base_function import base_function

import logging

@define
class Load(base_function):
    
    def __call__(self, line, registers, addresses, values, devices):
        """"""
        args = line.split("(")[1].strip(")").split(",")
        logging.debug(f"Load arguments: {args}")
        reg_a =  self.get_register(args[0].strip(), registers)  # Register A (5 bits)
        address = self.get_address(args[1].strip(), addresses)  # Address (24 bits)
        logging.debug(f"Register A: {reg_a}, Address: {address}")
        binary_instruction = (
            "001" + reg_a.binary_value[0] + address.binary_value + reg_a.binary_value[1:]
        )
        logging.debug(f"Load instruction: {binary_instruction}")
        hex_instruction = self.binary_to_hex(binary_instruction)
        return hex_instruction
        
