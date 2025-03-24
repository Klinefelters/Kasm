from attr import define

@define
class BaseKeyword:
    keyword: str = None

    def parse(self, **kwargs) -> str:
        raise NotImplementedError("parse method not implemented")