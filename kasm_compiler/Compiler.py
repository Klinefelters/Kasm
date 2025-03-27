from kasm_compiler.Lexer import Lexer
from kasm_compiler.Parser import Parser
from attr import define
import logging

@define
class Compiler:
    lexer: Lexer = Lexer()
    parser: Parser = Parser()
    variables: dict = {}

    def compile_kasm(self, file_path):

        tokens = self.lexer.analyse_file(file_path)

        compiled_code, self.variables = self.parser.parse_lines(tokens, self.variables)
        
        
        output_path = file_path.replace(".kasm", ".bin")

        with open(output_path, 'w') as output_file:
            output_file.write("\n".join(compiled_code))
        logging.info(f"Compiled to {output_path}")