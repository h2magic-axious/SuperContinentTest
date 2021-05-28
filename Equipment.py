from common import const

class Equipment:
    def __init__(self, name, kwargs:dict):
        self.name = name

        self.health = kwargs.get(const.HEALTH)
        self.defense = kwargs.get(const.DEFENSE)
        self.type_ = kwargs.get(const.TYPE)