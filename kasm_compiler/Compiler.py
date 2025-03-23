from kasm_compiler.Lexer import Lexer
from kasm_compiler.Parser import Parser
from kasm_compiler.Assembler import Assembler
from attr import define
import logging

@define
class Compiler:
    lexer: Lexer = Lexer()
    parser: Parser = Parser()
    assembler: Assembler = Assembler()

    def compile_kasm(self, file_path):
        lines = self.lexer.analyse_file(file_path)
        

        

        compiled_code = []
        
        
        output_path = file_path.replace(".kasm", ".bin")

        with open(output_path, 'w') as output_file:
            output_file.write("\n".join(compiled_code))
        print(f"Compiled to {output_path}")