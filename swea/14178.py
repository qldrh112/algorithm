def solution(n, d):
    # 분무기가 최대한 커버할 수 있는 범위
    d = 2 * d + 1

    if n % d:
        answer = n // d + 1
    else:
        answer = n // d

    return answer


T = int(input())
for t in range(T):
    N, D = map(int, input().split())
    print(f'#{t+1} {solution(N, D)}')