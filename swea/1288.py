def count_goat(goat):
    """
    params goat: 처음 주어진 양의 수(int)
    return: 누적하여 0~9까지 볼 수 있는 양 세기
    """
    n = 0
    counts = [0] * 10

    while counts != [1] * 10:
        num = (n+1) * goat
        while num != 0:
            if counts[num % 10] == 0:
                counts[num % 10] += 1
            num //= 10
        n += 1
    return n * goat

T = int(input())
for x in range(T):
    N = int(input())
    print(f'#{x+1} {count_goat(N)}')