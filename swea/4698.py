def solution(d, a, b):
    return is_contain_certain_num(d, seive_of_eratosthenes(a, b))


def seive_of_eratosthenes(start, end):
    """
    소수를 걸러내는 함수
    """
    result = 0
    limit = int(end ** 0.5) + 1
    end += 1
    is_primes = [True] * end  # 모든 수를 소수라고 가정
    is_primes[0] = is_primes[1] = 0  # 0과 1은 소수가 아님

    for i in range(2, limit):  # 시작부터 n의 제곱근까지만 검정하면 됨
        if is_primes[i]:  # 이 수가 소수라면 이 수를 곱의 피연산으로 활용한 값은 모두 소수
            for j in range(i * i, end, i):
                is_primes[j] = False

    return [idx for idx in range(start, end) if is_primes[idx]]


def is_contain_certain_num(num, primes):
    """
    특별한 소수인지 확인하는 함수
    """
    result = 0
    for prime in primes:
        # 10의 배수를 계속 나누어 그 글자가 특별한 수인지 확인함
        while prime >= 1:
            # int로 묶지 않으면 소수점이 튀어나옴
            if int(prime % 10) == num:
                result += 1
                break  # while
            else:
                prime /= 10
    return result

# def solution(d, a, b):
#     # 소수 목록 추출
#     primes = segmented_sieve(a, b)
#     # 특정 숫자 d를 포함하는 소수 개수 계산
#     return count_special_primes(d, primes)
#
#
# def segmented_sieve(start, end):
#     """
#     구간 에라토스테네스의 체: [start, end] 범위의 소수를 찾는 함수
#     """
#     limit = int(end ** 0.5) + 1
#     is_prime_small = [True] * limit
#     is_prime_range = [True] * (end - start + 1)
#
#     # 작은 범위(2 ~ √end)에서 소수 판별
#     for i in range(2, limit):
#         if is_prime_small[i]:
#             for j in range(i * i, limit, i):
#                 is_prime_small[j] = False
#
#             # 구간 내의 배수를 지우기
#             first_multiple = max(i * i, (start + i - 1) // i * i)
#             for j in range(first_multiple, end + 1, i):
#                 is_prime_range[j - start] = False
#
#     # 구간 내의 소수 목록 반환
#     return [x for x in range(start, end + 1) if is_prime_range[x - start]]
#
#
# def count_special_primes(num, primes):
#     """
#     주어진 소수 목록에서 특정 숫자 num이 포함된 소수의 개수를 세는 함수
#     """
#     num_str = str(num)
#     return sum(1 for prime in primes if num_str in str(prime))


if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        D, A, B = map(int, input().split())
        print(f'#{t + 1} {solution(D, A, B)}')