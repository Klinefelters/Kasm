from attr import define
from kasm_compiler.operators.base_operator import BaseOperator

@define
class Sub(BaseOperator):
    name: str = 'Sub'
    operator: str = '-'