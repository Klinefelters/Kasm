from logging import debug, error, warning, info
from attr import define

from kasm_compiler.syntaxes import OPS, VARS
from kasm_compiler.syntaxes.args import Register
from kasm_compiler.syntaxes.variables import Label



@define
class Assembler:
    line_num: int = 0
    vars: dict = {}
    vars_pointer: int = 0
    binary_instructions: list = []

    def handle_code(self, keyword, args):
        args = args.split(",") if "," in args else [args]
        args = [arg.strip() for arg in args]  
        
        if keyword in OPS.keys():
            op = OPS[keyword]
            op.line = self.line_num
            if keyword =="LDR" and args[1] in self.vars.keys():
                var = self.vars[args[1]]
                if not issubclass(args[0].__class__, Register): 
                    tmp = Register()
                    tmp.initialize(args[0], self.line_num)
                    reg = tmp
                else:
                    reg = args[0]
                if var.address in range(0, 0xFF):
                    tmp = [f"01100{var.address:08b}{reg}"]
                elif var.address in range(0xFF, 0xFFFF):
                    tmp = [
                        f"01001{var.low_addr:08b}101", 
                        f"01000{var.high_addr:08b}{reg}",
                        f"0010000{reg}101{reg}"
                    ]
                else:
                    error(f"VALUE ERROR: The address '{var.address}' on line {self.line_num} exceeds the maximum value of 65535.")
                    exit(1)

                self.binary_instructions = [*self.binary_instructions, *tmp]
                return
            self.binary_instructions = [*self.binary_instructions, *op.assemble(args)]

    def handle_vars(self, keyword, args):
        args = args.split(" ", 1)
        if ":" not in keyword:
            error(f"SYNTAX ERROR: Invalid variable declaration '{keyword}' on line {self.line_num}.")
            exit(1)
        if len(args) != 2:
            error(f"SYNTAX ERROR: Variable declaration on line {self.line_num} requires a type and value.")
            exit(1)
        if args[0] not in VARS.keys():
            error(f"SYNTAX ERROR: Invalid variable type '{args[0]}' on line {self.line_num}.")
            exit(1)
         
        var = VARS[args[0]].copy()
        var.address = self.vars_pointer
        assembly_instructions = var.initialize(args[1], self.line_num)
        for instruction in assembly_instructions:
            key, args = instruction.strip().split(" ", 1)
            self.handle_code(key, args)

        self.vars[keyword.split(":")[0].strip()] = var
        self.vars_pointer += var.next_address

    def handle_vars_start(self, assembly_code):
        """Handle the start of the code section."""
        # Reset the registers used to define variables
        self.binary_instructions.append(f"0011010000000000") 
        self.binary_instructions.append(f"0011010100100100")
        self.binary_instructions.append(f"0011010101101101")
        for line in assembly_code:
            line = line.strip().split(";")[0].strip()
            if line.startswith("@") and line.endswith(":"):
                label = Label()
                label.address = self.vars_pointer
                label.next_address += 1
                self.vars[line.strip(":")] = label
                self.vars_pointer += label.next_address


    def compile_code(self, assembly_code):
        """Compile a list of assembly instructions into binary."""

        current_section = None
        for self.line_num, line in enumerate(assembly_code, start=1):
            
            line = line.strip().split(";")[0] # Remove comments
            if line == "": continue
            
            split = line.strip().split(" ", 1)
            
            if len(split) == 1:
                keyword = split[0]
                args = ""
            else:
                keyword, args = split[0], split[1]

            debug(f"Processing line {self.line_num}: {keyword} {args}")

            if keyword == "section":
                current_section = args.strip()
                if current_section == ".vars":
                    self.handle_vars_start(assembly_code)
                continue

            if current_section == ".vars":
                self.handle_vars(keyword, args)
            
            elif current_section == ".code":
                if line.strip().endswith(":") and line.strip().startswith("@"):
                    label = self.vars[line.strip().strip(":")]
                    instructions = label.initialize(len(self.binary_instructions), self.line_num)
                    
                    for instruction in instructions:
                        key, args = instruction.strip().split(" ", 1)
                        self.handle_code(key, args)
                self.handle_code(keyword, args)
                    
        self.binary_instructions.append('0000000000000000')
        self.binary_instructions.append('1111111111111111')
        return self.binary_instructions
