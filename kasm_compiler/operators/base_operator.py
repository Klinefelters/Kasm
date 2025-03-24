from attr import define

@define
class BaseOperator:
    name: str = None
    operator: str = None

    def parse(self, **kwargs) -> str:
        raise NotImplementedError("parse method not implemented")