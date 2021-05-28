from Soldier import Solider, victory, fighting
from common import const

SA = {
    const.HEALTH: 100,
    const.P_DAMAGE: 10,
    const.E_DAMAGE: 0,
    const.ARMOR: 0,
    const.SHIELD: 0,
    const.LOAD: 100,
    const.DODGE: 40
}

SB = {
    const.HEALTH: 100,
    const.P_DAMAGE: 10,
    const.E_DAMAGE: 0,
    const.ARMOR: 0,
    const.SHIELD: 0,
    const.LOAD: 100,
    const.DODGE: 40
}


def test(number=10000):
    sa_victory = 0
    sb_victory = 0
    tie = 0

    for _ in range(number):
        sa = Solider('SA', **SA)
        sb = Solider('SB', **SB)
        winner = fighting(sa, sb)
        if winner == sa.name:
            sa_victory += 1
        elif winner == sb.name:
            sb_victory += 1
        else:
            tie += 1

    print(f'SA胜利{sa_victory}场，胜率{round(sa_victory / number * 100, 2)}%')
    print(f'SB胜利{sb_victory}场，胜率{round(sb_victory / number * 100, 2)}%')
    print(f'平局{tie}场，平局率{round(tie / number * 100, 2)}%')


if __name__ == '__main__':
    test()
