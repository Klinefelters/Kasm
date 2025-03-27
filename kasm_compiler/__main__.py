import sys
import logging
from kasm_compiler.Compiler import Compiler
from kasm_compiler.tmp import compile_code
# def main():

#     file_path = sys.argv[1]
#     with open(file_path) as f:
#         assembly_code = f.readlines()
#     binary_instructions = compile_code(assembly_code)

#     with open(file_path.replace(".kasm", ".hex"), "w") as f:
#         for instruction in binary_instructions:
#             nibbles = [instruction[i:i + 4] for i in range(0, len(instruction), 4)]
#             hex_instruction = "".join([hex(int(nibble, 2))[2:] for nibble in nibbles])
#             f.write(hex_instruction + "\n")

def main():

    if len(sys.argv) < 2:
        print("Usage: kasm <file.kasm> -l <log_level>")
        sys.exit(1)

    if "-l" in sys.argv:
        log_level_str = sys.argv[sys.argv.index("-l") + 1]
        print(f"Setting log level to {log_level_str.upper()}")
        if log_level_str.upper() == "DEBUG":
            log_level = logging.DEBUG
        elif log_level_str.upper() == "INFO":
            log_level = logging.INFO
        elif log_level_str.upper() == "WARNING":
            log_level = logging.WARNING
        elif log_level_str.upper() == "ERROR":
            log_level = logging.ERROR
        elif log_level_str.upper() == "CRITICAL":
            log_level = logging.CRITICAL
    else:
        log_level = logging.INFO

    logging.basicConfig(
        level=log_level,
        format="%(asctime)s | %(name)s | %(levelname)s | %(message)s",
    )

    file_path = sys.argv[1]
    compiler = Compiler()
    compiler.compile_kasm(file_path)


if __name__ == "__main__":
    main()