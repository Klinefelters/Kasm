import sys
from coloredlogs import install
from kasm_compiler import Assembler
from logging import debug, error, warning, info


def main():
    dump_binary = False
    if len(sys.argv) < 2 or len(sys.argv) > 5 or ".kasm" not in sys.argv[1]: 
        print("Usage: kasm <file.kasm> -l <log_level>")
        sys.exit(1)

    if "-b" in sys.argv:
        dump_binary = True
    if "-l" in sys.argv:
        
        log_level_str = (sys.argv[sys.argv.index("-l") + 1])[0:].upper()
        if log_level_str not in ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]:
            install(level='INFO')
            warning("Invalid log level. Use DEBUG, INFO, WARNING, ERROR, or CRITICAL.")
            
        else:
            install(level=log_level_str)
            info("Log level set to %s", log_level_str)
    else:
        install(level='INFO')

    file_path = sys.argv[1]
    info("Assembling %s", file_path)
    with open(file_path) as f:
        assembly_code = f.readlines()
    binary_instructions = Assembler().compile_code(assembly_code)

    if dump_binary:
        bin_path = file_path.replace(".kasm", ".bin")
        with open(bin_path, "w") as f:
            for instruction in binary_instructions:
                f.write(instruction+ "\n")
        info("Binary dump complete. Output saved to %s", bin_path)
    
    hex_path = file_path.replace(".kasm", ".hex")
    with open(hex_path, "w") as f:
        for instruction in binary_instructions:
            nibbles = [instruction[i:i + 4] for i in range(0, len(instruction), 4)]
            hex_instruction = "".join([hex(int(nibble, 2))[2:] for nibble in nibbles])
            f.write(hex_instruction + "\n")
    info("Assembly complete. Output saved to %s", hex_path)



if __name__ == "__main__":
    main()