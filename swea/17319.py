import sys
sys.stdin = open('input.txt', 'r')

def solution(n, string):
    """
    메모리: 44,772 kb
    실행시간: 97 ms
    """
    # 홀수 자리는 무조건 실패
    if n % 2:
        return 'No'
    
    for i in range(n // 2):
        if string[i] != string[n // 2 + i]:
            return 'No'
    return 'Yes'


TC = int(input())
for t in range(TC):
    N = int(input())
    S = input()
    print(f'#{t+1} {solution(N, S)}')