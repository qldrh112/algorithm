"""
주어진 두 문자열의 최대 공통 부분 수열(Longest Common Sequence)의 길이를 계산하는 프로그램을 작성하시오.

예를 들어 "acaykp"와 "capcak"의 경우, 두 문자열의 최대 공통 부분 수열은 "acak"로 길이가 4이다.

최장 공통 부분문자열(Longest Common Substring)을 계산하는 것이 아님에 주의한다.

[입력]

첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

각 테스트 케이스의 첫째 줄에 두 문자열이 공백을 사이에 두고 주어진다.

각 문자열은 알파벳 소문자로만 구성되어 있음이 보장된다.

각 문자열의 길이는 1,000 이하의 자연수이다.

[출력]

각 테스트 케이스마다 ‘#T’(T는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고, 최대 공통 부분 수열의 길이를 출력한다.

[입력]
1
acaykp capcak

-> acak

[출력]
#1 4
"""
import sys

sys.stdin = open('input.txt', 'r')


def solution(s1, s2):
    # s1 < s2가 되게 정렬
    if s1 > s2:
        s2, s1 = s1, s2
    dp = [0] * len(s2)

    for i in range(len(s2)):
        for j in range(min(i + 1, len(s1))):
            if s1[j] == s2[i]:
                dp[i] += 1


    print(s1, s2)
    return 'k' in s2


if __name__ == '__main__':
    T = int(input())
    for x in range(T):
        input_string1, input_string2 = input().split()
        print(f'#{x + 1} {solution(input_string1, input_string2)}')
