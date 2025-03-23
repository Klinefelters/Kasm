from attr import define

@define
class BaseOperator:
    name: str = None
    operator: str = None