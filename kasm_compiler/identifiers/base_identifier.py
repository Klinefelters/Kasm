from attr import define

@define
class BaseIdentifier:
    identifier: str = None
    name: str = None
    value: any = None

    def parse(self, **kwargs):
        raise NotImplemented