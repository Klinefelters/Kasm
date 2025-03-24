from attr import define
from kasm_compiler.identifiers.base_identifier import BaseIdentifier
from kasm_compiler.identifiers import IDENTIFIERS
from kasm_compiler.keywords.base_keyword import BaseKeyword
from kasm_compiler.keywords import KEYWORDS
from kasm_compiler.operators.base_operator import BaseOperator
from kasm_compiler.operators import OPERATORS

from logging import debug, error


@define
class Parser:
    def parse_lines(self, lines:list, variables:dict):
        parsed_lines = []
        for line in lines:
            parsed_line, variables = self.parse_line(line, variables)
            parsed_lines.extend(parsed_line)
        return parsed_lines, variables


    def parse_line(self, line:list, variables:dict):
        debug(f"Parsing line: {line}")
        parsed_lines = []

        if issubclass(type(line[0]), BaseOperator):
            error("Lines cannot start with an operator")
            raise Exception("Lines cannot start with an operator")

        elif issubclass(type(line[0]), BaseIdentifier):
            debug(f"Found Identifier: {line[0].identifier}")
            line[0].name = line[1]
            line[0].value = line[3]
            variables[line[0].name] = line[0]
        
        elif issubclass(type(line[0]), BaseKeyword):
            parsed_lines.append(line[0].parse(variables=variables, remaining_tokens=line[1:]))
        
        elif line[0] in variables.keys():
            left = line[0]
            right = line[2:]
            print(self.process_arithmetic(left, right, line[1], variables))
            
        
        return parsed_lines, variables
    
    def process_arithmetic(self, left, right:list, operator, variables:dict):
        print(f"Processing: {left} {operator} {right}\n")
        if left[0] in variables.keys():
            left = variables[left[0]]

        if len(right) == 1:
            if right[0] in variables.keys():
                right = variables[right[0]]
            
            print(f"Parsed: {operator.parse(ra=left, rb=right)}\n")
            return(f"{left} {operator} {right}")
        elif right[1].operator in OPERATORS.keys():
            new_right = right[2:]
            new_left = right[0]
            return(f'{left} {operator} {self.process_arithmetic(new_left, new_right, right[1], variables)}')
        else:
            error("Invalid arithmetic operation")
            raise Exception("Invalid arithmetic operation")