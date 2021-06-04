import json

from Soldier import Solider, fighting
from Equipment import Equipment
from common import const, core

import numpy as np
import matplotlib.pyplot as plt

with open('resource/soldiers.json', 'r', encoding='utf-8') as f:
    SOLIDER_MAP = json.load(f)

with open('localization/zh_cn.txt', 'r', encoding='utf-8') as f:
    LOCALIZATION = dict()
    for line in f:
        code, value = line.strip().split('=')
        LOCALIZATION[code] = value


def test(SA, SB, number=10000):
    sa_victory = 0
    sb_victory = 0
    tie = 0

    for _ in range(number):
        sa = Solider(LOCALIZATION[SA] + 'A', SOLIDER_MAP[SA])
        sb = Solider(LOCALIZATION[SB] + 'B', SOLIDER_MAP[SB])

        winner = fighting(sa, sb)
        # print(f"第{_ + 1}回合：{winner}胜利")

        if winner == sa.name:
            sa_victory += 1
        elif winner == sb.name:
            sb_victory += 1
        else:
            tie += 1

    return sa_victory / number, sb_victory / number, tie / number


if __name__ == '__main__':
    A = 'alien_warrior'
    B = 'psionic_warrior'

    a, b, t = test(A, B)
    # result = []
    # for i in range(10, 90):
    #     SA[const.DODGE] = i
    #     result.append(test(SA, SB))

    print('【{} A】胜率{:.2%}'.format(LOCALIZATION[A], a))
    print('【{} B】胜率{:.2%}'.format(LOCALIZATION[B], b))
    print('平局率{:.2%}'.format(t))

    # plt.figure(1)
    # x = [i for i in range(10, 90)]
    # plt.plot(x, [i[0] for i in result], 'b-')
    # plt.plot(x, [i[2] for i in result], 'r--')
    # plt.show()
