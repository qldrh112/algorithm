import sys
sys.stdin = open('input.txt', 'r')
from itertools import permutations

def solution(n):
    """
    메모리: 49,320 kb
    실행시간: 174 ms
    """
    multiple_list, length = same_digit_multiple_num(n)
    combination_list = make_combination(n, length)
    for num in combination_list:
        if num in multiple_list:
            return 'possible'
    return 'impossible'

def same_digit_multiple_num(num):
    """
    자릿수가 바뀌지 않는 배수를 반환하는 함수
    """
    digit, i = 1, 1
    while num > 10 * digit:
        digit *= 10
        i += 1
    return [x * num for x in range(2, 10) if x * num <= 10 * digit], i

def make_combination(num, length):
    """
    순열을 통해 숫자 조합을 반환하는 함수
    """
    permutation = list(permutations(range(length), length))
    result = [0] * len(permutation)
    for i in range(len(permutation)):
        comb = 0
        for idx, k in enumerate(permutation[i]):
            # k는 num의 인덱스로 뽑아내고
            # length - i는 10의 제곱수
            # num[k]는 num // 10 ** (length - k - 1) - 10 * num // 10 ** (length - k) 
            comb += (num // 10 ** (length - k - 1) - 10 * (num // 10 ** (length - k))) * 10 ** (length - idx - 1)
        result[i] = comb
    return result

T = int(input())
for t in range(T):
    N = int(input())
    print(f'#{t + 1} {solution(N)}')


def solution(n):
    sorted_n = sorted(str(n))
    multiplier = 2
    while True:
        multiplied = n * multiplier
        print(sorted(str(multiplied)))
        if len(str(multiplied)) > len(str(n)):
            break
        if sorted(str(multiplied)) == sorted_n:
            return 'possible'
        multiplier += 1
    return 'impossible'

T = int(input())
for t in range(T):
    N = int(input())
    print(f'#{t + 1} {solution(N)}')
