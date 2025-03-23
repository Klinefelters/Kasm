from attr import define
from KasmCompiler.functions.base_function import base_function

import logging

@define
class Jump(base_function):
    
    def __call__(self, line, registers, addresses, values, devices):
        """"""
        args = line.split("(")[1].strip(")").split(",")
        logging.debug(f"Jump arguments: {args}")
        address = self.get_address(args[0].strip(), addresses)  # Address (24 bits)
        logging.debug(f"Address: {address}")
        binary_instruction = (
            "1000" + address.binary_value + "0000"
        )
        logging.debug(f"Jump instruction: {binary_instruction}")
        hex_instruction = self.binary_to_hex(binary_instruction)
        return hex_instruction
        
