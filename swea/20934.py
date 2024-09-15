def solution(cups, alarm):
    """
    메모리: 43,248 kb
    실행시간: 139 ms
    """
    idx = cups.index('o')
    if not alarm:
        return idx
    else:
        return 1 if (idx % 2 and alarm % 2 == 0) or (idx % 2 == 0 and alarm % 2) else 0


T = int(input())
for t in range(T):
    S, K = input().split()
    print(f'#{t + 1} {solution(S, int(K))}')