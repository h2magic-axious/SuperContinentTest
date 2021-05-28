import random

from common import const


class Solider:
    def __init__(self, name, **kwargs):
        self.name = name
        self.health = kwargs.get(const.HEALTH)
        self.p_damage = kwargs.get(const.P_DAMAGE)
        self.e_damage = kwargs.get(const.E_DAMAGE)
        self.armor = kwargs.get(const.ARMOR)
        self.shield = kwargs.get(const.SHIELD)

        self.weight = 0
        self.load = kwargs.get(const.LOAD)

        self.base_dodge = kwargs.get(const.DODGE)
        self.dodge = self.base_dodge * (1 + self.weight / self.load) / 100

        self.arms = []

    def update_dodge(self):
        self.dodge = self.base_dodge * (1 + self.weight / self.load) / 100

    def dead(self):
        return self.health <= 0

    def attack(self, other):
        # 被攻击方闪避失败
        if random.random() < other.dodge:
            p_damage = self.p_damage * (1 - other.armor * const.S / (1 + other.armor * const.S))
            e_damage = self.e_damage * (1 - other.shield * const.S / (1 + other.shield * const.S))
            other.health -= p_damage + e_damage


def victory(s1: Solider, s2: Solider):
    s1_dead = s1.dead()
    s2_dead = s2.dead()

    if not s1_dead and not s2_dead:
        return 'c'  # continue
    elif s1_dead and not s2_dead:
        return s2.name
    elif not s1_dead and s2_dead:
        return s1.name
    else:
        return None


def fighting(s1: Solider, s2: Solider):
    w = 'c'
    while w == 'c':
        s1.attack(s2)
        s2.attack(s1)

        w = victory(s1, s2)

        if w is None:
            return None
    return w
