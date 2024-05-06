def solution(n, subscriber1, subscriber2):
    min_v = max(0, subscriber1 + subscriber2 - n)
    max_v = min(subscriber1, subscriber2)
    return max_v, min_v


T = int(input())
for t in range(T):
    N, A, B = map(int, input().split())
    print(f'#{t + 1}', *solution(N, A, B))
