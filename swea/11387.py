# import sys
# sys.stdin = open('input.txt', 'r')

# def solution(damage, level, N):
#     rank = 0
#     for n in range(N):
#         rank += 1 + (level * n) / 100
#     return int(rank * damage)


# T = int(input())
# for t in range(T):
#     D, L, N = map(int, input().split())
#     print(f'#{t+1} {solution(D, L, N)}')


import sys
sys.stdin = open('input.txt', 'r')

def solution(damage, level, N):
    total = 0
    for n in range(N):
        total += (1 + (level * n) / 100) * damage
    return total


T = int(input())
for t in range(T):
    D, L, N = map(int, input().split())
    print(f'#{t+1} {solution(D, L, N)}')