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
            
            tokens = line.strip().split()
            keyword = tokens[0]
            args = [token.strip(",") for token in tokens[1:]]  # Remove commas and whitespace from arguments
            debug(f"Processing line {self.line_num}: {keyword} with arguments {args}")  # Debug statement to show the current line being processed
            
            if keyword in OPS.keys():
                op = OPS[keyword]
                op.line = self.line_num
                debug(op.assemble(args)) 
        
        return self.binary_instructions
