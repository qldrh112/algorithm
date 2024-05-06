"""
메모리: 61,196 kb
실행시간: 197 ms
"""

def arr_palindrome_check(arr) -> int:
    if N == 1:
        return 64

    cnt = 0

    # 열, 행 동시 이동
    for k in range(8):

        # 포인터 1
        for i in range(8 - N + 1):

            if arr[k][i:i+N] == arr[k][i:i+N][::-1]:
                cnt += 1

            row_tmp = ''
            # 포인터 2
            for j in range(i, i + N):
                row_tmp += arr[j][k]

            # 회문 확인
            if row_tmp == row_tmp[::-1]:
                cnt += 1

    return cnt


for t in range(10):
    N = int(input())
    input_arr = [input() for _ in range(8)]
    print(f'#{t + 1} {arr_palindrome_check(input_arr)}')