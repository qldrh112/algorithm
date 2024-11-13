import sys
sys.stdin = open('input.txt', 'r')

"""
1. + 모양 탐색
2. x 모양 탐색
3. 큰 놈 반환
"""

def sum_col_row(arr):
    max_v = 0
    tmp = 0
    for col in range(N):
        for row in range(N):
            tmp = sum([arr[col][j] for j in range(N)]) + sum([arr[i][row] for i in range(N)]) - arr[col][row]
            if max_v < tmp:
                max_v = tmp
    return max_v

def sum_diag(arr):
    

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    input_arr = [list(map(int, input().split())) for _ in range(N)]
