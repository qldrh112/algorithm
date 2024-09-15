import sys
sys.stdin = open('input.txt', 'r')

# def solution(n, limit, arr):
#     """
#     메모리: 54,608 kb
#     실행시간: 9,664 ms

#     n: arr의 길이
#     arr: [[맛1, 칼로리1], [맛2, 칼로리2], ..., ]
#     """
#     answer = 0
#     for i in range(2**n, 0, -1):
#         answer = max(answer, calc_best_taste(n, bin(i)[2:].zfill(n), arr, limit))
#     return answer

# def calc_best_taste(n, binary, arr, limit):
#     """
#     제한 칼로리보다 적은 조합에서 맛의 총합을 반환하는 함수
#     """
#     choices = [arr[i] for i in range(n) if binary[i] == '1']
#     taste, calories = 0, 0
#     for choice in choices:
#         calories += choice[1]
#         if calories <= limit:
#             taste += choice[0]
#         else:
#             return 0
#     return taste

def solution(n, limit, arr):
    dp = [0] * (limit + 1)
    
    for taste, calorie in arr: 
        # 100, 200
        for j in range(limit, calorie - 1, -1):
            # 1000 -> 200
            dp[j] = max(dp[j], dp[j - calorie] + taste)
            # dp[1000] = max(df[1000], df[800] + 100)
            # dp[999] = max(df[999], df[799] + 100)
    print('현재 배열은', dp)
    
    return max(dp)

T = int(input())
for t in range(T):
    N, L = map(int, input().split())
    hamburgers = [list(map(int, input().split())) for _ in range(N)]    
    print(f'#{t + 1} {solution(N, L, hamburgers)}')