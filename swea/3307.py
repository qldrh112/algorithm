import sys
sys.stdin = open('input.txt', 'r')

def solution(n, seq):
    """
    메모리: 48,936 kb
    실행시간: 151 ms
    """
    lis = [1] * n
    for i in range(n):
        for j in range(i):
            if seq[i] > seq[j]:
                lis[i] = max(lis[i], lis[j] + 1)
    return max(lis)


T = int(input())
for t in range(T):
    N = int(input())
    input_seq = list(map(int, input().split()))
    print(f'#{t+1} {solution(N, input_seq)}')