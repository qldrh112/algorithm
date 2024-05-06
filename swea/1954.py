def draw_snail(n):
    """
    n: 달팽이의 크기(int, n*n)
    return: 달팽이를 그린 2차원 리스트
    """
    # 2차원 리스트 생성
    snail = [[0] * n for _ in range(n)]
    # col = 0
    # row = 0
    # for num in range(1, n**2+1):
    #     snail[col][row] = num
    #     if row + 1 < n and snail[col][row+1] == 0:
    #         row += 1
    #     elif col + 1 < n and snail[col+1][row] == 0:
    #         col += 1
    #     elif 0 <= row - 1 and snail[col][row-1] == 0:
    #         row -= 1
    #     else:
    #         col -= 1
    # return snail
    
    # 자연수 num
    num = 1
    col = 0
    row = 0
    # 0, 0에 1은 고정
    snail[col][row] = num

    while num < n**2:
        # 우
        while row + 1 < n and snail[col][row+1] == 0:
            row += 1
            num += 1
            snail[col][row] = num
        # 하
        while col + 1 < n and snail[col+1][row] == 0:
            col += 1
            num += 1
            snail[col][row] = num
        # 좌
        while 0 <= row - 1 and snail[col][row-1] == 0:
            row -= 1
            num += 1
            snail[col][row] = num
        # 우
        while 0 <= col - 1 and snail[col-1][row] == 0:
            col -= 1
            num += 1
            snail[col][row] = num

    return snail


T = int(input())
for t in range(T):
    N = int(input())
    arr = draw_snail(N)
    # 출력합니다.
    print(f'#{t+1}')
    for i in range(N):
        for j in range(N):
            if j < N-1:
                print(arr[i][j], end=' ')
            else:
                print(arr[i][j])