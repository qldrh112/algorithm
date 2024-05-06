"""
메모리: 62,508 kb
실행시간: 208 ms
"""
def max_sum(arr):
    max_v = 0
    for i in range(100):
        row_sum = sum(arr[i][:])
        col_sum = sum([arr[j][i] for j in range(100)])
        max_v = max(max_v, row_sum, col_sum)

    return max_v


for _ in range(10):
    t = int(input())
    input_arr = [list(map(int, input().split())) for _ in range(100)]
    print(f'#{t} {max_sum(input_arr)}')