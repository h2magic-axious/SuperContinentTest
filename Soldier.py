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
            const.P_DAMAGE: kwargs.get(const.P_DAMAGE, 0),
            const.E_DAMAGE: kwargs.get(const.E_DAMAGE, 0),
            const.ARMOR: kwargs.get(const.ARMOR, 0),
            const.SHIELD: kwargs.get(const.SHIELD, 0)
        }

        self.weight = 0
        self.load = kwargs.get(const.LOAD)

        self.base_dodge = 10
        self.dodge = 0
        self.update_dodge()

        self.equipments = dict()
        self.equipments_type_map = {
            const.P_DAMAGE: 0,
            const.E_DAMAGE: 0,
            const.ARMOR: 0,
            const.SHIELD: 0
        }

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
            self.wear(p_damage, e_damage)
            other.wear(p_damage, e_damage, False)

    def add_equipment(self, e_object):
        weight = self.weight + e_object.weight
        if weight > self.load:
            return

        self.equipments[e_object.name] = e_object
        self.equipments_type_map[e_object.type_] += 1
        self.weight = weight

        self.update_dodge()
        self.attributes[e_object.type_] += e_object.data

    def del_equipment(self, e_name):
        e_object = self.equipments[e_name]
        self.equipments_type_map[e_object.type_] -= 1
        del self.equipments[e_name]

        self.weight -= e_object.weight
        self.update_dodge()
        self.attributes[e_object.type_] -= e_object.data

    def wear(self, p_damage, e_damage, attack=True):
        for e_name, e_object in self.equipments.items():
            if attack:
                if e_object.type_ == const.P_DAMAGE:
                    e_object.wear(p_damage / self.equipments_type_map[const.P_DAMAGE])
                if e_object.type_ == const.E_DAMAGE:
                    e_object.wear(e_damage / self.equipments_type_map[const.E_DAMAGE])
            else:
                if e_object.type_ == const.ARMOR:
                    e_object.wear(p_damage / self.equipments_type_map[const.ARMOR])
                if e_object.type_ == const.SHIELD:
                    e_object.wear(e_damage / self.equipments_type_map[const.SHIELD])
            if e_object.health <= 0:
                self.del_equipment(e_name)

    def __repr__(self):
        t = Texttable()
        t.set_deco(Texttable.HEADER)
        t.set_cols_align(['l', 'l'])
        t.add_rows([
            [self.name, ''],
            ['生命值', self.health],
            ['物理攻击', self.attributes[const.P_DAMAGE]],
            ['灵能攻击', self.attributes[const.E_DAMAGE]],
            ['护甲', self.attributes[const.ARMOR]],
            ['护盾', self.attributes[const.SHIELD]],
            ['闪避', self.dodge],
            ['装备', [f"{e.name}:{e.health} " for k, e in self.equipments.items()]],
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
