from common import const


class Equipment:
    def __init__(self, name, kwargs: dict):
        self.name = name

        self.health = kwargs.get(const.HEALTH, 0)
        self.data = kwargs.get(const.DATA, 0)
        self.type_ = kwargs.get(const.TYPE, 0)
        self.weight = kwargs.get(const.WEIGHT, 0)

    def wear(self, attack):
        if self.type_ == const.P_DAMAGE or self.type_ == const.E_DAMAGE:
            self.health -= const.WS * attack
        if self.type_ == const.ARMOR or self.type_ == const.SHIELD:
            self.health -= const.AS * attack
