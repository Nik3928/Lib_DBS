class Group:
    """ Named group of permissions"""
    def __init__(self, id_: int, name: str, permissions: list[str]):
        self.id = id_
        self.name = name
        self.permissions = permissions
