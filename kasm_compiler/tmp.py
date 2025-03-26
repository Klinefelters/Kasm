# Define the opcode and operand mappings based on the README.md
OPCODES = {
    "NOOP": "000",
    "MATH": "001",
    "LOAD": "010",
    "LOADI": "011",
    "STORE": "100",
    "JMPIF": "101",
    "RIO": "110",
    "WIO": "110",
    "HALT": "111"
}

MATH_OPS = {
    "ADD": "0000", "SUB": "0001", "MUL": "0010", "DIV": "0011",
    "REM": "0100", "SLL": "0101", "SLR": "0110", "SAR": "0111",
    "AND": "1000", "NAND": "1001", "ORR": "1010", "NOR": "1011",
    "XOR": "1100", "XNOR": "1101", "NMOV": "1110", "MOV": "1111"
}

JMPIF_OPS = {
    "GRT": "000", "EQL": "001", "LST": "010",
    "UGT": "011", "UEQ": "100", "ULT": "101",
    "NOOP": "110", "JMP": "111"
}

def register_to_binary(register):
    """Convert a register (e.g., R0, R1) to a 3-bit binary string."""
    if register.startswith("R") and register[1:].isdigit():
        reg_num = int(register[1:])
        if 0 <= reg_num < 8:
            return f"{reg_num:03b}"
    raise ValueError(f"Invalid register: {register}")

def device_to_binary(device):
    """Convert a device (e.g., D0, D1) to a 3-bit binary string."""
    if device.startswith("D") and device[1:].isdigit():
        reg_num = int(device[1:])
        if 0 <= reg_num < 8:
            return f"{reg_num:03b}"
    raise ValueError(f"Invalid device: {device}")

def immediate_to_binary(immediate, bits=8):
    """Convert an immediate value to a binary string."""
    if 0 <= immediate < (1 << bits):
        return f"{immediate:0{bits}b}"
    raise ValueError(f"Immediate value out of range: {immediate}")

def assemble_instruction(instruction):
    """Assemble a single instruction into a 16-bit binary string."""
    parts = instruction.split()
    keyword = parts[0].upper()

    if keyword == "NOOP":
        return "0000000000000000"

    elif keyword in MATH_OPS:
        op = MATH_OPS[keyword]
        rd = register_to_binary(parts[1])
        ra = register_to_binary(parts[2])
        rb = register_to_binary(parts[3])
        return f"001{op}{rd}{ra}{rb}"

    elif keyword == "LOAD":
        rd = register_to_binary(parts[1])
        ra = register_to_binary(parts[2])
        return f"0100000{rd}{ra}000"

    elif keyword == "LOADI":
        mode = parts[1]
        imm = immediate_to_binary(int(parts[2]))
        rb = register_to_binary(parts[3])
        return f"011{mode}{imm}{rb}"

    elif keyword == "STORE":
        ra = register_to_binary(parts[1])
        rb = register_to_binary(parts[2])
        return f"1000000000{ra}{rb}"

    elif keyword == "JMPIF":
        op = JMPIF_OPS[parts[1].upper()]
        rb = register_to_binary(parts[2])
        return f"101{op}0000000{rb}"

    elif keyword == "RIO":
        rd = register_to_binary(parts[1])
        rb = device_to_binary(parts[2])
        return f"11000{rd}000{rb}"

    elif keyword == "WIO":
        ra = register_to_binary(parts[1])
        rb = device_to_binary(parts[2])
        return f"11001{ra}000{rb}"

    elif keyword == "WIOI":
        mode = parts[1]
        imm = immediate_to_binary(int(parts[2]))
        rb = device_to_binary(parts[3])
        return f"1101{mode}{imm}{rb}"

    elif keyword == "HALT":
        return "1111111111111111"

    else:
        raise ValueError(f"Unknown instruction: {keyword}")

def compile_code(assembly_code):
    """Compile a list of assembly instructions into binary."""
    binary_instructions = []
    for line in assembly_code:
        line = line.strip()
        if line and not line.startswith("#"):  # Ignore empty lines and comments
            binary_instructions.append(assemble_instruction(line))
    return binary_instructions
