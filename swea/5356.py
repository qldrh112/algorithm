def solution(col_length, arr):
    answer = ''
    # 개수 설정할 때 가장 긴 녀석의 길이로 해야 한다.
    for col in range(col_length):
        for row in range(5):
            try:
                answer += arr[row][col]
            except IndexError:
                continue

    return answer


T = int(input())
for t in range(T):
    input_arr = [list(input()) for _ in range(5)]
    n = max([len(input_arr[x]) for x in range(5)])
    print(f'#{t+1} {solution(n, input_arr)}')