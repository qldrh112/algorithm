import math

def find_prime_number(x):
    """
    메모리: 106,300 kb
    실행시간: 2,366 ms
    """
    for num in range(2, int(math.sqrt(x)) + 2):
        div, mod = divmod(x, num)
        if not mod:
            return False
    return True

def solution():
    prime_number_map = {k: False for k in range(2, 1000000 + 1)}
    for num in range(2, 1000000):
        if find_prime_number(num):
            prime_number_map[num] = True
    return [2] + [key for key in prime_number_map.keys() if prime_number_map[key]]
    
print(*solution())


import math

def sieve_of_eratosthenes(limit):
    """
    2의 배수, 3의 배수, n의 제곱근의 배수 다 쳐내는 방식
    메모리: 61,900 kb
    실행시간: 208 ms
    """
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False  # 0과 1은 소수가 아님
    for start in range(2, int(math.sqrt(limit)) + 1):
        if sieve[start]:
            for multiple in range(start * start, limit + 1, start):
                sieve[multiple] = False
    return [num for num, is_prime in enumerate(sieve) if is_prime]

print(*sieve_of_eratosthenes(1000000))


"""
# 알고리즘 문제에서는 사용 불가
from sympy import primerange

def solution():
    return list(primerange(2, 1000001))

print(*solution())
"""