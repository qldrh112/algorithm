def rotation(n, matrix):
    """
    params n: 행렬의 크기 (n * n)
    params matrix: 행렬
    return: 행렬을 90도 돌린 행렬
    """
    rotated_arr = [[0] * n for _ in range(n)]

    for col in range(n):
        for row in range(n):
            rotated_arr[row][n-1-col] = matrix[col][row]

    return rotated_arr

T = int(input())
for t in range(T):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 90도, 180도, 270도 돌린 행렬을 생성합니다.
    rotation90 = rotation(N, matrix)
    rotation180 = rotation(N, rotation90)
    rotation270 = rotation(N, rotation180)

    # 출력합니다.
    print(f'#{t+1}')
    output = [rotation90, rotation180, rotation270]
    for col in range(N):
        line_count = 0
        for i in range(len(output)):
            for row in range(N):
                line_count += 1
                # 한 줄이 채워지면
                if line_count == N * 3:
                    print(output[i][col][row])
                # 한 행렬이 마무리되면
                elif row == N-1:
                    print(output[i][col][row], end=' ')
                else:
                    print(output[i][col][row], end='')