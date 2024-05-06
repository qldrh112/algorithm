def solution(c1, c2):
    success = c1 * c2

    s1 = (1 - c1) * success
    s2 = c1 * (1 - q) * success

    if s1 < s2:
        return 'YES'
    else:
        return 'NO'


T = int(input())
for t in range(T):
    p, q = map(float, input().split())
    print(f'#{t+1} {solution(p, q)}')