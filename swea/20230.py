# import sys
# sys.stdin = open('input.txt', 'r')

"""
1. 가장 긴 가로 줄과 세로 줄의 조합 -> 가운데 있는 수가 변수
2. 델타로 뻗어나가기
"""

def max_col_row(n, arr):
    """
    n: 풍선 배열의 크기
    arr: 풍선 배열
    return: 최대로 획득할 수 있는 보너스 점수(int)
    """

    max_v = 0
    for col in range(n):
        for row in range(n):
            tmp = arr[col][row]
            for di, dj in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
                # 방향 전환할 때마다 i, j 초기화할 것
                i = col
                j = row
                while 0 <= i + di < n and 0 <= j + dj < n:
                    i += di
                    j += dj
                    tmp += arr[i][j]
            if max_v < tmp:
                max_v = tmp
    return max_v


T = int(input())
for t in range(T):
    N = int(input())
    input_arr = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{t+1} {max_col_row(N, input_arr)}')