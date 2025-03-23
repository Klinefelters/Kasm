from attr import define

@define
class BaseKeyword:
    name: str = None
    operands: list = []