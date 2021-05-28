import random

from common import const


class Solider:
    def __init__(self, name, kwargs: dict):
        self.name = name
        # self.id = ident
        # self.belong = belong

        self.health = kwargs.get(const.HEALTH)
        self.p_damage = kwargs.get(const.P_DAMAGE)
        self.e_damage = kwargs.get(const.E_DAMAGE)
        self.armor = kwargs.get(const.ARMOR)
        self.shield = kwargs.get(const.SHIELD)

        self.weight = 0
        self.load = kwargs.get(const.LOAD)

        self.base_dodge = kwargs.get(const.DODGE)
        self.dodge = 0
        self.update_dodge()

        self.arms = dict()

    def update_dodge(self):
        dodge = self.base_dodge * (1 + self.weight / self.load) / 100
        if dodge > 0.9:
            self.dodge = 0.9
        else:
            self.dodge = dodge

    def attack(self, other):
        # 被攻击方闪避失败
        if random.random() > other.dodge or other.dodge == 0:
            p_damage = self.p_damage * (1 - other.armor * const.S / (1 + other.armor * const.S))
            e_damage = self.e_damage * (1 - other.shield * const.S / (1 + other.shield * const.S))
            other.health -= p_damage + e_damage


def fighting(s1: Solider, s2: Solider):
    while True:
        s1.attack(s2)
        s2.attack(s1)

        if s1.health <= 0 and s2.health <= 0:
            return None

        if s1.health <= 0 and s2.health > 0:
            return s2.name

        if s2.health <= 0 and s1.health > 0:
            return s1.name
