import random

from texttable import Texttable

from common import const, core


def compute_damage(attack, defense):
    return attack * (1 - defense * const.S / (1 + defense * const.S))


class Solider:
    def __init__(self, name, kwargs: dict):
        self.name = name
        # self.id = ident
        # self.belong = belong

        self.health = kwargs.get(const.HEALTH)
        self.attributes = {
            const.P_DAMAGE: kwargs.get(const.P_DAMAGE),
            const.E_DAMAGE: kwargs.get(const.E_DAMAGE),
            const.ARMOR: kwargs.get(const.ARMOR),
            const.SHIELD: kwargs.get(const.SHIELD)
        }

        self.weight = 0
        self.load = kwargs.get(const.LOAD)

        self.base_dodge = kwargs.get(const.DODGE)
        self.dodge = 0
        self.update_dodge()

        self.equipments = dict()

    def update_dodge(self):
        dodge = self.base_dodge * (1 - self.weight / self.load) / 100
        if dodge > 0.9:
            self.dodge = 0.9
        else:
            self.dodge = dodge

    def attack(self, other):
        # 被攻击方闪避失败
        if random.random() > other.dodge or other.dodge == 0:
            p_damage = compute_damage(self.attributes[const.P_DAMAGE], other.attributes[const.ARMOR])
            e_damage = compute_damage(self.attributes[const.E_DAMAGE], other.attributes[const.SHIELD])
            other.health -= p_damage + e_damage

    def add_equipment(self, e_object):
        weight = self.weight + e_object.weight
        if weight > self.load:
            return

        self.equipments[e_object.name] = e_object
        self.weight = weight

        self.update_dodge()
        self.attributes[e_object.type_] += e_object.data

    def __repr__(self):
        t = Texttable()
        t.set_deco(Texttable.HEADER)
        t.set_cols_align(['c', 'c'])
        t.add_rows([
            [self.name, ''],
            ['生命值', self.health],
            ['物理攻击', self.attributes[const.P_DAMAGE]],
            ['灵能攻击', self.attributes[const.E_DAMAGE]],
            ['护甲', self.attributes[const.ARMOR]],
            ['护盾', self.attributes[const.SHIELD]],
            ['闪避', self.dodge],
            ['', '']
        ])

        return t.draw()


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
