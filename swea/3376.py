import sys
sys.stdin = open('input.txt', 'r')

# def solution(n):
#     """
#     메모리: 45,056 kb
#     실행시간: 124 ms
#     """
#     tri_lengths = [1, 1, 1, 2, 2, 3]
#     if n <= 6:
#         return tri_lengths[n - 1]
#     else:
#         for _ in range(n - 6):
#             tri_lengths.append(tri_lengths[-1] + tri_lengths[-5])
#         return tri_lengths[-1]

# T = int(input())
# for t in range(T):
#     N = int(input())
#     print(f'#{t + 1} {solution(N)}')

def solution(n):
    """
    메모리: 45,616 kb
    실행시간: 115 ms
    """
    if n <= 6:
        return [1, 1, 1, 2, 2, 3][n-1]

    p1, p2, p3, p4, p5, p6 = 1, 1, 1, 2, 2, 3
    for _ in range(7, n+1):
        next_p = p6 + p2
        p1, p2, p3, p4, p5, p6 = p2, p3, p4, p5, p6, next_p
    return p6

T = int(input())
for t in range(T):
    N = int(input())
    print(f'#{t + 1} {solution(N)}')
