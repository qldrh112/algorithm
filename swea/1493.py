def solution(p1, q1):
    # 좌표로 수 구하기

    def coordinate(p):
        i, j = 1, 1
        while j <= 10000:
            print(i, j)
            if p == i:
                py = 1
                px = j
                return px, py
            elif p < i:
                py = i - p + 1
                px = j - py + 1
                return px, py
            else:
                i += j
                j += 1

    for i in range(1, 10):
        print(i,':', coordinate(i))




T = int(input())
for t in range(T):
    p, q = map(int, input().split())
    print(f'#{t+1} {solution(p, q)}')