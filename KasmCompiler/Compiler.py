from KasmCompiler.constants import INSTRUCTION_SET, ALU_INSTRUCTION_SET
from KasmCompiler.declarables.Address import Address
from KasmCompiler.declarables.Register import Register
from KasmCompiler.declarables.Value import Value
from KasmCompiler.declarables.Device import Device
from KasmCompiler.functions import functions
import logging


class Compiler:
    def __init__(self):
        self.registers = []
        self.addresses = []
        self.values = []
        self.devices = []
        self.next_register = 0  # Start at 0 for 5-bit binary
        self.num_address = 0  # Start at 0 for 24-bit binary
        self.functions = functions
        self.current_address = 0

    def declare_register(self, name):
        if self.next_register >= 32:
            logging.error("Maximum number of registers (32) exceeded.")
            raise ValueError("Maximum number of registers (32) exceeded.")
        self.registers.append(Register(name, self.next_register))
        self.next_register += 1

    def declare_address(self, name, address):
        if self.num_address >= 2**24:
            logging.error("Maximum number of addresses (2^24) exceeded.")
            raise ValueError("Maximum number of addresses (2^24) exceeded.")
        self.addresses.append(Address(name, binary_value=address))
        self.num_address += 1
    
    def declare_int(self, name, value: int):
        if value >= 2**24:
            logging.error("Maximum integer value (2^24) exceeded.")
            raise ValueError("Maximum integer value (2^24) exceeded.")
        self.values.append(Value.from_int(name, value))

    def declare_device(self, name, value: int):
        if value >= 32:
            logging.error("Maximum integer value 32 exceeded.")
            raise ValueError("Maximum integer value 32 exceeded.")
        value = int(value)
        print(Device.from_index(name, value))
        self.devices.append(Device.from_index(name, value))

    def declare_Char(self, name, value: chr):
        self.values.append(Value.from_ascii(name, value))

    def get_register(self, name):
        for register in self.registers:
            if register.name == name:
                return register
        logging.error(f"Register not found: {name}")
        raise ValueError(f"Register not found: {name}")
    
    def get_address(self, name):
        for address in self.addresses:
            if address.name == name:
                return address
        logging.error(f"Address not found: {name}")
        raise ValueError(f"Address not found: {name}")
    
    def get_value(self, name):
        for value in self.values:
            if value.name == name:
                return value
        logging.error(f"Value not found: {name}")
        raise ValueError(f"Value not found: {name}")

    def binary_to_hex(self, binary_string):
        """Convert a binary string to a hexadecimal string in chunks of 4 bits."""
        hex_output = ""
        for i in range(0, len(binary_string), 4):
            chunk = binary_string[i:i+4]
            hex_output += format(int(chunk, 2), 'X')
        logging.debug(f"Converted binary to hex: {binary_string} -> {hex_output}")
        return hex_output

    def compile_kasm(self, file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()

        compiled_code = []
        for line in lines:
            logging.debug(f"Processing line: {line}")
            line = line.strip()
            if not line or line.startswith("//"):  # Skip empty lines or comments
                logging.debug("Skipping line, it is a comment")
                continue

            # Handle declarations
            if " = new register" in line:
                name = line.split(" = ")[0]
                logging.debug("Found register declaration: " + name)
                self.declare_register(name)
                continue
            elif " = new address" in line:
                name = line.split(" = ")[0]
                logging.debug("Found address declaration: " + name)
                self.declare_address(name, self.current_address)
                compiled_code.append(self.functions["NoOp"](line, self.registers, self.addresses, self.values, self.devices))
                self.current_address+=1
                continue
            elif " = new int" in line:
                # name = new int(42)
                name = line.split(" = ")[0]
                value = int(line.split('(')[1].strip(')'))
                logging.debug("Found int declaration: " + name + " = " + str(value))
                self.declare_int(name, value)
                continue
            elif " = new char" in line:
                # name = new char("a")
                name = line.split(" = ")[0]
                value = line.split('("')[1][0]
                logging.debug("Found char declaration: " + name + " = " + value)
                self.declare_Char(name, value)
                continue
            elif " = new device" in line:
                # name = new int(42)
                name = line.split(" = ")[0]
                value = int(line.split('(')[1].strip(')'))
                logging.debug("Found device declaration: " + name + " = " + str(value))
                self.declare_device(name, value)
                continue

            if any(name in line for name in self.functions.keys()):
                logging.debug(f"Found function call: {line}")
                name = line.split("(")[0]
                compiled_code.append(self.functions[name](line, self.registers, self.addresses, self.values, self.devices))
                if name == "Jump":
                    compiled_code.append(self.functions["NoOp"](line, self.registers, self.addresses, self.values, self.devices))
                    self.current_address+=1
                self.current_address+=1
                continue

            if any(op in line for op in ALU_INSTRUCTION_SET.keys()):
                # Parse the Data command
                args = line.split("(")[1].strip(")").split(",") # Extract arguments inside parentheses
                logging.debug(f"Data arguments: {args}")
                alu_operation = line.split("(")[0]  # ALU operation (e.g., Add, Sub, Mov)
                reg_a = self.get_register(args[0].strip()).binary_value  # Register A (5 bits)
                reg_b = self.get_register(args[1].strip()).binary_value  # Register B (5 bits)
                reg_d = self.get_register(args[2].strip()).binary_value  # Destination Register (5 bits)
                # Construct the binary representation
                opcode = INSTRUCTION_SET["Data"]
                alu_opcode = ALU_INSTRUCTION_SET[alu_operation]  # Default ALU opcode (can be customized later)
                logging.debug(f"ALU Opcode: {alu_opcode}, Registers: {reg_a}, {reg_b}, {reg_d}")
                binary_instruction = (
                    opcode + alu_opcode + "000000000" + reg_a + reg_b + reg_d
                )
                logging.debug(f"Data instruction: {binary_instruction}")
                # Convert binary to hexadecimal using the helper function
                hex_instruction = self.binary_to_hex(binary_instruction)
                compiled_code.append(hex_instruction)
                self.current_address+=1
                continue


            else:
                raise ValueError(f'Unknown instruction: {line}')

        # Write the compiled output
        compiled_code.append(self.functions["Halt"](line, self.registers, self.addresses, self.values, self.devices))
        compiled_code.append(self.functions["NoOp"](line, self.registers, self.addresses, self.values, self.devices))
        compiled_code.append(self.functions["NoOp"](line, self.registers, self.addresses, self.values, self.devices))
        output_path = file_path.replace(".kasm", ".bin")
        with open(output_path, 'w') as output_file:
            output_file.write("\n".join(compiled_code))
        print(f"Compiled to {output_path}")