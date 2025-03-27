from attr import define
from logging import debug, error

from kasm_compiler.identifiers import IDENTIFIERS, BaseIdentifier, Immediate
from kasm_compiler.keywords import KEYWORDS, BaseKeyword
from kasm_compiler.operators import OPERATORS, BaseOperator
from kasm_compiler.token import Token


@define
class Parser:
    def parse_lines(self, lines:list, variables:dict):
        parsed_lines = []
        for line in lines:
            parsed_line, variables = self.parse_line(line, variables)
            parsed_lines.extend(parsed_line)
        return parsed_lines, variables


    def parse_line(self, line:list, variables:dict):
        parsed_lines = []
        
        for token in line:
            if type(token) is str and token in variables.keys():
                line[line.index(token)] = variables[token]

        debug(f"Parsing line: {line}")

        if issubclass(type(line[0]), BaseIdentifier):
            debug(f"Found Identifier: {line[0].identifier}")
            variables[line[1]] = line[0].enstantiate(line[1], line[2])
            debug(f"Added variable: {line[1]} = {variables[line[1]].value}")
        
        elif issubclass(type(line[0]), BaseOperator):
            debug(f"Found Operator: {line[0].operator}")
            parsed_lines.append(line[0].parse(line[1:]))
        
        elif issubclass(type(line[0]), BaseKeyword): 
            debug(f"Found Keyword: {line[0].keyword}")
            parsed_lines.append(line[0].parse(line[1:]))
            
        else:
            error(f"Unknown token: {line[0]}")

        return parsed_lines, variables