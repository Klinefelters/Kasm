from attr import define
from logging import debug
from kasm_compiler.operators import OPERATORS
from kasm_compiler.identifiers import IDENTIFIERS
from kasm_compiler.keywords import KEYWORDS

@define
class Lexer:
    
    def analyse_file(self, file_path):
        lines_of_tokens = []
        with open(file_path, 'r') as file:
            for line in file.readlines():
                
                line = self.clean_line(line)
                if not line:
                    continue
                
                debug(f"Tokenizing line: {line}")
                tokens = self.tokenize(line)
                debug(f"Tokens: {tokens}\n")
                lines_of_tokens.append(tokens)
        return lines_of_tokens
            

    def clean_line(self, line):
        line = line.strip()
        if not line or line.startswith("//"):
            return None
        return line
    
    def tokenize(self, line):
        tmp = line.split(',')
        tokens = []
        for token in tmp:
            token = token.strip()

            if token in OPERATORS.keys():
                tokens.append(OPERATORS[token]())
            elif token in IDENTIFIERS.keys():
                tokens.append(IDENTIFIERS[token]())
            elif token in KEYWORDS.keys():
                tokens.append(KEYWORDS[token]())
            else:
                tokens.append(token)

        return tokens