from logging import error

def register_to_binary(register):
    """Convert a register (e.g., R0, R1) to a 3-bit binary string."""
    if register.startswith("R") and register[1:].isdigit():
        reg_num = int(register[1:])
        if 0 <= reg_num < 8:
            return f"{reg_num:03b}"
    error(f"Invalid register: {register}")

def register_address_to_binary(register):
    """Convert a register address (e.g., [R0], [R1]) to a 3-bit binary string."""
    if register.startswith("[R") and register[2:-1].isdigit():
        reg_num = int(register[2:-1])
        if 0 <= reg_num < 8:
            return f"{reg_num:03b}"
    error(f"Invalid register: {register}")

def device_to_binary(device):
    """Convert a device (e.g., D0, D1) to a 3-bit binary string."""
    if device.startswith("D") and device[1:].isdigit():
        reg_num = int(device[1:])
        if 0 <= reg_num < 8:
            return f"{reg_num:03b}"
    error(f"Invalid device: {device}")

def hex_to_binary(hex, bits=8):
    """Convert a decimal value to a binary string."""
    if hex.startswith("0x") and int(hex[2:], 16) < (1 << bits):
        return f"{int(hex[2:], 16):0{bits}b}"
    error(f"Hex value out of range: {hex}")

def decimal_to_binary(decimal, bits=8):
    """Convert a decimal value to a binary string."""
    if 0 <= int(decimal) < (1 << bits):
        return f"{int(decimal):0{bits}b}"
    error(f"Decimal value out of range: {decimal}")

def immediate_to_binary(immediate, bits=8):
    """Convert an immediate value to a binary string."""
    if immediate.startswith("0x"):
        return hex_to_binary(immediate, bits)
    else:
        return decimal_to_binary(immediate, bits)
