from attr import define
from kasm_compiler.operators.base_operator import BaseOperator
from kasm_compiler.identifiers.register import Register

@define
class Add(BaseOperator):
    name: str = 'Add'
    operator: str = '+'

    def parse(self, **kwargs) -> str:
        if 'ra' in kwargs.keys() and 'rb' in kwargs.keys():
            ra = kwargs['ra']
            rb = kwargs['rb']
        else:
            raise Exception("Missing required arguments")
        
        if 'rd' in kwargs.keys():
            rd = kwargs['rd']
        else:
            rd = rb
        
        if type(ra) is not Register: 
            raise TypeError("ra must be a register but ra = " + ra)

        if type(rb) is not Register: 
            raise TypeError("rb must be a register but ra = " + rb)

        if type(rd) is not Register: 
            raise TypeError("rd must be a register but ra = " + rd)

        return '001' + '0090' + ra.parse() + rb.parse() + rd.parse()
        
        
        
        
        
