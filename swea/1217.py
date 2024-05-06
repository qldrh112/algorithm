"""
메모리: 58,284 kb
실행시간: 152 ms
"""

def N_square(base, exponent):
    if exponent == M:
        print(f'#{t} {base}')
        return
    else:
        N_square(base*N, exponent+1)
        return


for _ in range(10):
    t = int(input())
    N, M = map(int, input().split())
    base = N
    if not M:
        print(f'#{t}', 1)
    N_square(base, 1)