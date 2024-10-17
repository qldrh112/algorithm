import sys

sys.stdin = open('input.txt', 'r')

def sieve_of_eratosthenes(size):  
    limit = size // 2 + 1
    is_prime = [True] * size
    is_prime[0] = is_prime[1] = False
    for i in range(2, limit):
        if is_prime[i]:
            for j in range(i * i, size, i):
                is_prime[j] = False
    return [i for i, boolean in enumerate(is_prime) if boolean]

# 에라토스테네스의 체로 999까지의 소수를 구하기
primes = sieve_of_eratosthenes(1000)
# dp[n][k] = n을 k개의 소수로 나눌 수 있는 경우의 수
dp = [[0] * 4 for _ in range(1000 + 1)]

# k가 1인 경우
for prime in primes:
    dp[prime][1] = 1

# k가 2인 경우
for i in range(5, 1000 + 1):
    value = 0
    for j in range(2, i // 2 + 1):
        value += dp[j][1] * dp[i - j][1]
    dp[i][2] = value

# k가 3인 경우
for i in range(7, 1000 + 1):
    value = 0
    for x in primes:
        if x > i:
            break   # for x in primes
        for y in primes:
            # x가 y보다 크고, i를 초과하였다면
            if x > y or x + y >= i:
                continue    # for y in primes
            z = i - (x + y)
            # y와 크거나 같거나 primes 안에 속한다면
            if z >= y and z in primes:
                value += 1
    dp[i][3] = value

def solution(num):    
    return dp[num][3]

if __name__ == '__main__':
    T = int(input())
    for x in range(T):
        N = int(input())
        print(f'#{x + 1} {solution(N)}')