from attr import define

import logging

@define
class base_function:

    def binary_to_hex(self, binary_string):
        """Convert a binary string to a hexadecimal string in chunks of 4 bits."""
        hex_output = ""
        for i in range(0, len(binary_string), 4):
            chunk = binary_string[i:i+4]
            hex_output += format(int(chunk, 2), 'X')
        logging.debug(f"Converted binary to hex: {binary_string} -> {hex_output}")
        return hex_output
    
    def get_register(self, name, registers):
        for register in registers:
            if register.name == name:
                return register
        logging.error(f"Register not found: {name}")
        raise ValueError(f"Register not found: {name}")
    
    def get_address(self, name, addresses):
        for address in addresses:
            if address.name == name:
                return address
        logging.error(f"Address not found: {name}")
        raise ValueError(f"Address not found: {name}")
    
    def get_value(self, name, values):
        for value in values:
            if value.name == name:
                return value
        logging.error(f"Value not found: {name}")
        raise ValueError(f"Value not found: {name}")
    
    def get_device(self, name, devices):
        print(devices)
        for device in devices:
            if device.name == name:
                return device
        logging.error(f"Device not found: {name}")
        raise ValueError(f"Device not found: {name}")
    
    def __call__(self, line, registers, addresses, values, devices):
        logging.error("Function not implemented.")
        raise NotImplementedError("Function not implemented.")
    