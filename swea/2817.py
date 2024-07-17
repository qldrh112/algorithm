"""
def solution(seq, n, tar):
    # DP 배열을 초기화, dp[i]는 합이 i인 부분집합의 수를 의미
    dp = [0] * (tar + 1)
    dp[0] = 1  # 합이 0인 경우는 항상 1가지 (공집합)

    for num in seq:
        for i in range(tar, num - 1, -1):
            dp[i] += dp[i - num]
            print(dp)

    return dp[tar]

# 입력 처리 부분
T = int(input())
for x in range(T):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    print(f'#{x+1} {solution(A, N, K)}')

"""


import sys
sys.stdin = open('input.txt', 'r')

def discrimination(val, tar):
    if val == tar:
        return 1
    else:
        return 0
    
def solution(seq, n, tar):
    """
    메모리: 72,976 kb
    실행시간: 921 ms
    """
    result = 0
    def sum_of_subset(level, n, val, tar, seq):
        nonlocal result
        if level == n:
            result += discrimination(val, tar)
        elif val > tar:
            return
        else:
            for bool in [True, False]:
                if bool:
                    sum_of_subset(level+1, n, val+seq[level], tar, seq)
                else:
                    sum_of_subset(level+1, n, val, tar, seq)

    # 수열의 합이 K보다 크거나 수열에서 가장 작은 값이 K보다 작다면 0을 반환
    if sum(seq) < tar and min(seq) > tar:
        return 0
    else:
        sum_of_subset(0, n, 0, tar, seq)
        return result


T = int(input())
for x in range(T):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    print(f'#{x+1} {solution(A, N, K)}')
    result = 0

