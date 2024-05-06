def solution(n, arr):
    answer = sum([case[0] * case[1] for case in arr])
    return answer


T = int(input())
for t in range(T):
    N = int(input())
    input_arr = [list(map(float, input().split())) for _ in range(N)]
    print(f'#{t+1} {solution(N, input_arr)}')
