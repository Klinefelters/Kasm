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

    def handle_code(self, keyword, args):
        args = args.split(",") if "," in args else [args]
        args = [arg.strip() for arg in args]  
        
        if keyword in OPS.keys():
            op = OPS[keyword]
            op.line = self.line_num
            self.binary_instructions = [*self.binary_instructions, *op.assemble(args)]

    def compile_code(self, assembly_code):
        """Compile a list of assembly instructions into binary."""

        current_section = None
        for self.line_num, line in enumerate(assembly_code, start=1):
            # self.line_num += 1
            
            line = line.strip().split(";")[0] # Remove comments
            if line == "": continue
            
            keyword, args = line.strip().split(" ", 1)
            
            if keyword == "section":
                current_section = args.strip()
                continue

            if current_section == ".vars":
                pass
            
            elif current_section == ".code":
                debug(f"Processing line with keyword: {keyword} and args: {args}")  # Debug statement to show the current line being processed
                self.handle_code(keyword, args)
                    
        self.binary_instructions.append('0000000000000000')
        self.binary_instructions.append('1111111111111111')
        return self.binary_instructions
