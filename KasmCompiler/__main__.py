import sys
import logging
from KasmCompiler.Compiler import Compiler


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