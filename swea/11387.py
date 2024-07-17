import sys
sys.stdin = open('input.txt', 'r')

# def solution(damage, level, N):
#     """
#     메모리: 52,364 kb
#     실행시간: 1,245 ms
#     """
#     total = 0
#     for n in range(N):
#         total += (n * level + 100) * damage
#     return total


# T = int(input())
# for t in range(T):
#     D, L, N = map(int, input().split())
#     print(f'#{t+1} {solution(D//100, L, N)}')

def solution(D, L, N):
    """
    메모리: 53,332 kb
    실행시간: 1,188 ms
    """
    total_damage = D * (N + (L / 100) * (N * (N - 1) / 2))
    return round(total_damage)

T = int(input())
for t in range(T):
    D, L, N = map(int, input().split())
    print(f'#{t+1} {solution(D, L, N)}')