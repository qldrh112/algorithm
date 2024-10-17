import sys
sys.stdin = open('input.txt', 'r')

def solution(n, a, b):
    """
    메모리: 49,068 kb
    실행시간: 647 ms
    """
    """
    param: n -> int
    param: a -> int
    param: b -> int
    return answer -> int
    """
    # n이 제곱수이면 항상 답은 0
    if int(n ** 0.5) ** 2 == n:
        return 0
    else:
        return find_min_value(n, a, b)

def find_min_value(n, a, b):
    """
    param: n -> int
    param: a -> int
    param: b -> int
    return answer -> int
    """
    min_value = float('inf')
    # 1부터 n의 제곱근까지 r에 값을 할당
    for r in range(1, int(n ** 0.5) + 1):
        # 1부터 r까지는 모두 검정했므로 c의 값을 r과 같게 설정
        c = r
        while r * c <= n:
            value = a * abs(r - c) + b * (n - r * c)
            min_value = min(min_value, value)
            c += 1
    return min_value


T = int(input())
for x in range(T):
    N, A, B = map(int, input().split())
    print(f'#{x + 1} {solution(N, A, B)}')