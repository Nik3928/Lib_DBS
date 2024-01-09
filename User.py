import Group


class User:
    def __init__(self, uid: str, name: str, groups: list[Group.Group]):
        self.uid = uid
        self.name = name
        self.groups = groups

    @property
    def permissions(self) -> list[str]:
        return sum([group.permissions for group in self.groups], start=[])

    def __repr__(self):
        return str(self.__dict__)

    def __str__(self):
        return self.__repr__()
