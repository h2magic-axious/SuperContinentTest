from common import const


class Equipment:
    def __init__(self, name, kwargs: dict):
        self.name = name

        self.health = kwargs.get(const.HEALTH)
        self.data = kwargs.get(const.DATA)
        self.type_ = kwargs.get(const.TYPE)
        self.weight = kwargs.get(const.WEIGHT)
