a = [0, 2, 3]
for t in range(10):
    N = int(input())
    input_arr = [list(input().split()) for _ in range(N)]
    for i in range(N-1, -1, -1):
        for j in a:
            print(i, j)
            print(input_arr)
            input_arr[i][j] = int(input_arr[i][j])
    tree = inorder_cal(N, input_arr)
    # 출력합니다.
    print(f'#{t+1} {int(tree[1])}')
