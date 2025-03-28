from logging import debug, error
from attr import define

from kasm_compiler.assembler.helpers import (
    device_to_binary, immediate_to_binary,
    register_address_to_binary, register_to_binary
)

# Define the opcode and operand mappings based on the README.md
OPCODES = {
    "NOP": "000", "MATH": "001", "LDR": "010",
    "LDL": "011", "LDH": "011", "STR": "100",
    "JMP": "101", "IN": "110", "OUT": "110",
    "OUTL": "110", "OUTH": "110", "HALT": "111"
}

MATH_OPS = {
    "ADD": "0000", "SUB": "0001", "MUL": "0010", "DIV": "0011",
    "REM": "0100", "SLL": "0101", "SLR": "0110", "SAR": "0111",
    "AND": "1000", "NAND": "1001", "OR": "1010", "NOR": "1011",
    "XOR": "1100", "XNOR": "1101", "NMOV": "1110", "MOV": "1111"
}

BRANCH_OPS = {
    "BSGT": "000", "BSEQ": "001", "BSLT": "010",
    "BGT": "011", "BEQ": "100", "BLT": "101", "JMP": "111"
}

@define
class Assembler:
    line_num: int = 0
    data: dict = {}
    vars: dict = {}
    subroutines: dict = {}
    labels: dict = {}
    binary_instructions: list = []

    def assemble_code(self, instruction):
        """Assemble a single instruction into a 16-bit binary string."""
        current_instructions = []
        parts = instruction.split()
        new_parts = []
        for part in parts[1:]:
            if part.startswith("//"):
                break
            new_parts.append(part.strip(","))
        parts = [parts[0], *new_parts]
        keyword = parts[0]
        debug(f"Parts: {parts}, Keyword: {keyword}")
        
        if keyword[0] == "@":
            self.labels[keyword[1:]] = len(self.binary_instructions)
        
        elif keyword in BRANCH_OPS:
            op = BRANCH_OPS[keyword]
            sub = parts[1]
            if sub in self.labels:
                sub = int(self.labels[sub])
                if sub < 256:
                    current_instructions.append(f"01100{sub:08b}111")
                elif sub < 65536:
                    subl = sub & 0xFF
                    subh = (sub >> 8) & 0xFF
                    current_instructions.append(f"01101{subh:08b}110")
                    current_instructions.append(f"01101{subl:08b}111")
                    current_instructions.append(f"0010000111110111")
                else:
                    error(f"Subroutine out of range: {sub}")
            current_instructions.append(f"101{op}0000000111")

        elif keyword in MATH_OPS:
            if keyword == "NMOV" or keyword == "MOV":
                rb = '000'
            else:
                rb = register_to_binary(parts[3])
            op = MATH_OPS[keyword]
            rd = register_to_binary(parts[1])
            ra = register_to_binary(parts[2])
            current_instructions.append(f"001{op}{rd}{ra}{rb}")
        
        elif keyword == "LDR":
            rd = register_to_binary(parts[1])
            ra = register_address_to_binary(parts[2])
            current_instructions.append(f"0100000{rd}{ra}000")

        elif keyword == "LDL":
            imm = immediate_to_binary(parts[2])
            rb = register_to_binary(parts[1])
            current_instructions.append(f"01100{imm}{rb}")
        
        elif keyword == "LDH":
            imm = immediate_to_binary(parts[2])
            rb = register_to_binary(parts[1])
            current_instructions.append(f"01101{imm}{rb}")

        elif keyword == "STR":
            ra = register_address_to_binary(parts[2])
            rb = register_to_binary(parts[1])
            current_instructions.append(f"1000000000{ra}{rb}")

        elif keyword == "IN":
            rd = register_to_binary(parts[1])
            rb = device_to_binary(parts[2])
            current_instructions.append(f"1100000{rd}000{rb}")

        elif keyword == "OUT":
            ra = register_to_binary(parts[1])
            rb = device_to_binary(parts[2])
            current_instructions.append(f"1100100{ra}000{rb}")

        elif keyword == "OUTL":
            imm = immediate_to_binary(parts[1])
            rb = device_to_binary(parts[2])
            current_instructions.append(f"11010{imm}{rb}")
        
        elif keyword == "OUTH":
            imm = immediate_to_binary(parts[1])
            rb = device_to_binary(parts[2])
            current_instructions.append(f"11011{imm}{rb}")

        elif keyword == "CALL":
            subroutine = parts[1]
            if subroutine in self.subroutines:
                sub = self.subroutines[subroutine]
                for instruction in sub:
                    current_instructions.append(instruction)
        
        elif keyword == "HALT":
            current_instructions.append("1111111111111111")
        
        elif keyword == "NOP":
            current_instructions.append("0000000000000000")
        
        else:
            error(f"Unknown instruction: {keyword}")
        return current_instructions

    def compile_code(self, assembly_code):
        """Compile a list of assembly instructions into binary."""
        
        current_section = None
        subroutine = False  
        subroutine_name = None 
        subroutine_lines = []

        for line in assembly_code:
            self.line_num += 1
            line = line.strip()
            if line.startswith("//"):
                continue
            if line.startswith("section."):
                current_section = line[8:]
                continue
            if current_section == "constants":
                continue
            if current_section == "variables":
                continue
            if current_section == "subroutines":
                if line and line.endswith(":"):
                    subroutine_name = line.split(":")[0]
                    subroutine = True
                    continue
                elif line and subroutine and line.startswith("END"):
                    subroutine = False
                    tmp = []
                    for l in subroutine_lines:
                        tmp = [*tmp, *self.assemble_code(l)]
                    self.subroutines[subroutine_name] = tmp
                elif line and subroutine:
                    subroutine_lines.append(line)
            if current_section == "instructions":
                if line:
                    self.binary_instructions= [*self.binary_instructions, *self.assemble_code(line)]

        return self.binary_instructions
