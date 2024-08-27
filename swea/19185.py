def solution(year, cheongan, gigi):
    s = (year - 1) % N
    t = (year - 1) % M
    return cheongan[s] + gigi[t]


TC = int(input())
for t in range(TC):
    N, M = map(int, input().split())
    input_list1 = list(input().split())
    input_list2 = list(input().split())
    Q = int(input())
    result = []
    for _ in range(Q):
        Y = int(input())
        result.append(solution(Y, input_list1, input_list2))
    print(f'#{t+1}', *result)
