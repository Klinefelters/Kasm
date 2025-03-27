from attr import define
from kasm_compiler.operators.base_operator import BaseOperator
from kasm_compiler.identifiers.register import Register

@define
class Add(BaseOperator):
    name: str = 'ADD'
    operator: str = '+'

    def parse(self, args) -> str:
        if len(args) != 3:
            raise ValueError("Add operator must have 3 arguments but has " + str(len(args)))
        
        for arg in args:
            if not isinstance(arg, Register):
                raise ValueError("Add operator arguments must be registers")
        [ra, rb, rd] = args

        return '001' + '0000' + ra.parse() + rb.parse() + rd.parse()
        
        
        
        
        
