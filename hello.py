import random


def monster(hp, gold):
    hp -= 4
    gold += 1

    return hp, gold


def merchant(hp, gold, level):
    if gold >= 2:
        hp += 5
        gold -= 2

    if hp > 10 + level:
        hp = 10 + level

    return hp, gold


def digging(gold):
    gold += 2

    return gold


if __name__ == "__main__":
    list_a = []
    count = 0
    for i in range(1):
        karma = 1
        step = 0
        while step < 50:
            hp = 10
            level = 0
            gold = 0
            killcount = 0
            print(f'이것은 {karma}번째 삶이다.')
            print(f'50걸음을 걸으면 해방될 수 있다.')
            while True:
                step += 1
                a = random.choice([1, 1, 1, 1, 1, 1, 2, 2, 3, 3])  # 1 = 괴물 / 2= 포션 / 3 = 득템  // 간단한 밸패 가능

                if a == 1:
                    print('괴물이다!')
                    hp, gold = monster(hp, gold)
                    if hp > 0:
                        print(f'용사는 괴물을 죽였다! 지금 체력은 {hp}이다. \n가진 돈은 {gold}gold이다.')
                        killcount += 1
                        if killcount % 4 == 0 and killcount != 0:
                            print('용사는 강해진 기분이다.... 최대체력이 1 증가하였다.')
                            level += 1
                    else:
                        print(f'체력이 없다. 죽을 것 같다....')
                elif a == 2:
                    if hp < 10:
                        hp, gold = merchant(hp, gold, level)
                        print(f'용사는 빨간포션을 샀다. 지금 체력은 {hp}이다.\n가진 돈은 {gold}gold이다.')
                else:
                    gold = digging(gold)
                    print(f'용사는 돈을을 주웠다. \n가진 돈은 {gold}gold이다.')

                if hp < 1:
                    karma += 1
                    print('=' * 50)
                    print(f'용사는 {step}걸음 만에 죽었다. 그의 레벨{level}이었다.\n{killcount}마리의 괴물을 죽였고, 가진 돈은 {gold}gold였다.')
                    print('=' * 50)
                    step = 0
                    hp = 10
                    gold = 0
                    killcount = 0
                    level = 0

                if step == 50:
                    break
        print('=' * 50)
        print(f'용사는 해방되었다.\n{karma}번째 환생의 결과다.... \n그의 레벨{level}이었다.\n{killcount}마리의 괴물을 죽였고, 가진 돈은 {gold}gold였다.')
        print('=' * 50)

        list_a.append([karma, level])

    for i, (hero, level) in enumerate(list_a):

        if hero == 1:
            print(f'{i}번째 용사는 환생없이 탈출하였다. 그는 운좋은 새끼이다. 도달한 레벨은 {level}이다.')
            count += 1

    print(f'운좋은 새끼는 {count}명이었다.')