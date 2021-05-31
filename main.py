import json

from Soldier import Solider, fighting
from Equipment import Equipment
from common import const, core

import numpy as np
import matplotlib.pyplot as plt


def test(SA, SB, number=10000):
    sa_victory = 0
    sb_victory = 0
    tie = 0

    for _ in range(number):
        sa = Solider('SA', SA)
        sb = Solider('SB', SB)

        winner = fighting(sa, sb)
        if winner == sa.name:
            sa_victory += 1
        elif winner == sb.name:
            sb_victory += 1
        else:
            tie += 1

    return sa_victory / number, sb_victory / number, tie / number


if __name__ == '__main__':
    SA = {
        const.HEALTH: 100,
        const.P_DAMAGE: 10,
        const.E_DAMAGE: 0,
        const.ARMOR: 0,
        const.SHIELD: 0,
        const.LOAD: 100,
        const.DODGE: 50
    }

    SB = {
        const.HEALTH: 100,
        const.P_DAMAGE: 10,
        const.E_DAMAGE: 0,
        const.ARMOR: 0,
        const.SHIELD: 0,
        const.LOAD: 100,
        const.DODGE: 50
    }

    with open("resource/equipment.json", 'r', encoding='utf-8') as f:
        equipment_map = json.load(f)

    a1 = Equipment('a1', equipment_map['armor'])
    s1 = Equipment('s1', equipment_map['shield'])

    sa = Solider('SA', SA)
    sb = Solider('SB', SB)

    sa.add_equipment(a1)
    sb.add_equipment(s1)

    print(sa)
    print(sb)

    a, b, t = test(SA, SB)
    # result = []
    # for i in range(10, 90):
    #     SA[const.DODGE] = i
    #     result.append(test(SA, SB))

    print('SA胜率{:.2%}'.format(a))
    print('SB胜率{:.2%}'.format(b))
    print('平局率{:.2%}'.format(t))

    # plt.figure(1)
    # x = [i for i in range(10, 90)]
    # plt.plot(x, [i[0] for i in result], 'b-')
    # plt.plot(x, [i[2] for i in result], 'r--')
    # plt.show()
