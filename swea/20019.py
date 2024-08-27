import sys
sys.stdin = open('input.txt', 'r')

# def solution(string):
#     """
#     메모리: 45,052 kb
#     실행시간: 120 ms
#     """
#     if is_palindrome([string], 0):
#         return 'YES'
#     else:
#         return 'NO'

# def is_palindrome(strings, i, n=2):
#     if i == n:
#         return True
#     else:
#         for string in strings:
#             if string == string[::-1]:
#                 return is_palindrome([string[:len(string) // 2], string[len(string) // 2 + 1:]], i + 1)
#             else:
#                 return False

# simple is best
def is_palindrome(string):
    n = len(string)
    mid = n // 2
    
    # 첫 번째 조건: 전체 문자열이 회문인지 확인
    if string != string[::-1]:
        return False
    
    # 두 번째 조건: 첫 번째 절반 부분이 회문인지 확인
    if string[:mid] != string[:mid][::-1]:
        return False
    
    # 세 번째 조건: 마지막 절반 부분이 회문인지 확인
    if string[-mid:] != string[-mid:][::-1]:
        return False
    
    return True

def solution(string):
    return 'YES' if is_palindrome(string) else 'NO'

T = int(input())
for t in range(T):
    S = input()
    print(f'#{t+1} {solution(S)}')


T = int(input())
for t in range(T):
    S = input()
    print(f'#{t+1} {solution(S)}')