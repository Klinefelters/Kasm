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

        

        if issubclass(type(line[0]), BaseOperator):
            error("Lines cannot start with an operator")
            raise Exception("Lines cannot start with an operator")
        
        if type(line[0]) is str and line[0] in variables.keys():
            left = line[0]
            right = line[2:]
            debug(self.process_arithmetic(left, right, line[1], variables))

        debug(f"Parsing line: {line}")

        if issubclass(type(line[0]), BaseIdentifier):
            debug(f"Found Identifier: {line[0].identifier}")
            variables[line[1]] = line[0].enstantiate(line[1], line[2])
            debug(f"Added variable: {line[1]} = {variables[line[1]].value}")
            return parsed_lines, variables
        

        for token in line:
            if type(token) is str and token in variables.keys():
                line[line.index(token)] = variables[token]
        
        
        if issubclass(type(line[0]), BaseKeyword): 
            debug(f"Found Keyword: {line[0].keyword}")
            parsed_lines.append(line[0].parse(line[1:]))
        
        return parsed_lines, variables
    
    def process_arithmetic(self, left, right:list, operator, variables:dict):
        debug(f"Processing: {left} {operator} {right}\n")
        if left[0] in variables.keys():
            left = variables[left[0]]

        if len(right) == 1:
            if right[0] in variables.keys():
                right = variables[right[0]]
            
            debug(f"Parsed: {operator.parse(ra=left, rb=right)}\n")
            return(right)
        elif right[1].operator in OPERATORS.keys():
            new_right = right[2:]
            new_left = right[0]
            right = self.process_arithmetic(new_left, new_right, right[1], variables)
            debug(f"Parsed: {operator.parse(ra=left, rb=right)}\n")
            return(right)
        else:
            error("Invalid arithmetic operation")
            raise Exception("Invalid arithmetic operation")