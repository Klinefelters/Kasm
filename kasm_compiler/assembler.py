from logging import debug, error
from attr import define

from kasm_compiler.syntaxes import OPS



@define
class Assembler:
    line_num: int = 0
    data: dict = {}
    vars: dict = {}
    labels: dict = {}
    data_pointer: int = 0
    binary_instructions: list = []

    def compile_code(self, assembly_code):
        """Compile a list of assembly instructions into binary."""
        for line in assembly_code:
            self.line_num += 1
            line = line.strip().split(";")[0]
            if line == "":
                continue
            
            keyword, args = line.strip().split(" ", 1)
            args = args.split(",") if "," in args else [args]
            args = [arg.strip() for arg in args]  
            debug(f"Processing line {self.line_num}: {keyword} with arguments {args}")  # Debug statement to show the current line being processed
            
            if keyword in OPS.keys():
                op = OPS[keyword]
                op.line = self.line_num
                self.binary_instructions = [*self.binary_instructions, *op.assemble(args)]
            debug(f"Binary Instructions: {self.binary_instructions[-1]}")
        self.binary_instructions.append('0000000000000000')
        self.binary_instructions.append('1111111111111111')
        return self.binary_instructions
