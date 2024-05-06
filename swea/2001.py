TC = int(input())

# TC만큼 반복
for q in range(TC):
    whole_lst = []
    output_lst = []
    M, N = map(int, input().split())
    p = M-N+1

    # 파리판 만들기
    for _ in range(M):
        input_lst = [input().split()]
        whole_lst.extend(input_lst)
        
    # 좌상단 좌표 때렸을 때 잡히는 파리 수

    for col in range(p):
        for row in range(p):
            tmp = 0
            for i in range(N):
                for j in range(N):
                    tmp += int(whole_lst[col+i][row+j])
            output_lst.append(tmp)

    # 가장 많이 잡힌 파리 수 뽑아 내기
    output = max(output_lst)
    print(f'#{q+1} {output}')
