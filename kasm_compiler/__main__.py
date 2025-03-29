import sys
from coloredlogs import install
from kasm_compiler import Assembler
import logging


def main():
    dump_binary = False
    if len(sys.argv) < 2 or len(sys.argv) > 4 or sys.argv[1] == "-h" or ".kasm" not in sys.argv[1]: 
        print("Usage: kasm <file.kasm> -l <log_level>")
        sys.exit(1)

    if "-b" in sys.argv:
        dump_binary = True
    if "-l" in sys.argv:
        
        log_level_str = (sys.argv[sys.argv.index("-l") + 1])[0:].upper()
        if log_level_str == "DEBUG":
            install(level='DEBUG')
        elif log_level_str == "INFO":
            install(level='INFO')
        elif log_level_str == "WARNING":
            install(level='WARNING')
        elif log_level_str == "ERROR":
            install(level='ERROR')
        elif log_level_str == "CRITICAL":
            install(level='CRITICAL')
    else:
        install(level='INFO')

    file_path = sys.argv[1]
    with open(file_path) as f:
        assembly_code = f.readlines()
    binary_instructions = Assembler().compile_code(assembly_code)

    if dump_binary:
        with open(file_path.replace(".kasm", ".bin"), "w") as f:
            for instruction in binary_instructions:
                f.write(instruction+ "\n")

    with open(file_path.replace(".kasm", ".hex"), "w") as f:
        for instruction in binary_instructions:
            nibbles = [instruction[i:i + 4] for i in range(0, len(instruction), 4)]
            hex_instruction = "".join([hex(int(nibble, 2))[2:] for nibble in nibbles])
            f.write(hex_instruction + "\n")



if __name__ == "__main__":
    main()