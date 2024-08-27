import sys
sys.stdin = open('input.txt', 'r')

# from math import ceil
# from collections import Counter

# def solution(n, li):
#     """
#     메모리: 53,576 kb
#     실행시간: 256 ms
#     """
#     i = 1
#     while i <= n:
#         n_digits = make_n_digits(n, i, li)
#         result = check_no_digits(Counter(n_digits).keys(), i)
#         if result >= 0:
#             return result
#         else:
#             i += 1
        
# def check_no_digits(values, i):
#     """
#     없는 수를 확인하고, 인덱스나 True를 반환하는 함수
#     """
#     target = 10 ** (i - 1) if i > 1 else 0
#     for num in values:
#         if num == float('inf'):
#             return -1
#         elif num == target:
#             target += 1
#             continue
#         else:
#             return target
#     return -1
    
# def make_n_digits(n, i, li):
#     """
#     리스트의 요소 n개를 합쳐 새로운 리스트로 반환하는 함수
#     n: 전체 숫자의 길이
#     i: 자리수
#     li: 숫자 리스트
#     """
#     return sorted([concat_nums(li[j : j + i], i) for j in range(n - i + 1)])
    
# def concat_nums(lst, i):
#     result = 0
#     for j in range(i):
#         result +=  lst[-1 - j] * (10 ** j)
#     return result if result >= 10 ** (i - 1) or i == 1 else float('inf')
    

# T = int(input())
# for t in range(T):
#     N = int(input())
#     li = []
#     while True:
#         if len(li) != N:
#             li.extend(list(map(int, input().split())))
#         else:
#             break   # while True
#     print(f'#{t + 1} {solution(N, li)}')


def solution(n, digits):
    """
    메모리: 51,208 kb
    실행시간: 183 ms
    """
    # 모든 수를 나타낼 수 있는지를 체크하는 배열
    can_make = [False] * 1001
    
    # 가능한 모든 부분 수열을 생성하여 체크
    for i in range(n):
        num = 0
        for j in range(i, n):
            num = num * 10 + digits[j]
            print(num)
            if num <= 1000:
                can_make[num] = True
            else:
                break
    
    # 1부터 시작하여 나타낼 수 없는 가장 작은 수 찾기
    for i in range(0, 1001):
        if not can_make[i]:
            return i
    return 1001  # 이 경우는 거의 발생하지 않음

T = int(input())
for t in range(T):
    N = int(input())
    digits = []
    while True:
        if len(digits) != N:
            digits.extend(list(map(int, input().split())))
        else:
            break
    print(f'#{t + 1} {solution(N, digits)}')
