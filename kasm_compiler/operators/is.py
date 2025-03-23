from attr import define
from kasm_compiler.operators.base_operator import BaseOperator

@define
class Is(BaseOperator):
    name: str = 'is'
    operator: str = '='