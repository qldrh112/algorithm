# 테스트 케이스 수 입력
TC = int(input())

# 테스트 케이스만큼 반복합니다.
for t in range(TC):
    pascal = []
    height = int(input())

    for col in range(height): # 0 1 2 
        tmp_list = []
        for row in range(col+1): # (0) (0,1) (0,1,2)
            
            # 각 높이의 마지막
            if row == col:
                tmp_list.append(1)

            # 각 높이의 처음
            elif row == 0:
                tmp_list.append(1)

            # 그 외
            else:
                tmp_list.append(pascal[col-1][row-1] + pascal[col-1][row])
            
        pascal.append(tmp_list)

    print(f'#{t+1}')
    for i in range(len(pascal)): # 0 1 2 3
        for j in range(len(pascal[i])): #0, 0,1
            if i == j:
                print(pascal[i][j])
            else:
                print(pascal[i][j], end= ' ')
