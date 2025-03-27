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
      final_code = []
      for line in compiled_code:
         if '\n' in line:
            [final_code.append(l) for l in line.strip().split('\n')]
         else:
            final_code.append(line)

      final_code.append('0000000000000000')
      final_code.append('1111111111111111')
         
      bin_path = file_path.replace(".kasm", ".bin")
      hex_path = file_path.replace(".kasm", ".hex")

      with open(file_path.replace(".kasm", ".bin"), 'w') as bin_file:
         bin_file.write("\n".join(final_code))
      logging.info(f"Compiled binary to {bin_path}")

      with open(file_path.replace(".kasm", ".hex"), 'w') as hex_file:
         hex_file.write("\n".join([hex(int(instruction, 2))[2:].zfill(4) for instruction in final_code]))
      logging.info(f"Compiled binary to {hex_path}")