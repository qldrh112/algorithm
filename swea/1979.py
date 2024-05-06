def word_sapce_in_puzzle(arr, N, K):
    count = 0
    for col in range(N):
        for row in range(N):
            if col<N-K+1 and row<N-K+1:
                if arr[col][row] == 1:
                    word_count = 0
                    # 행 검정
                    

                    # 열 검정
                    if col <= N-K:
                        word_count = 0
                        for k in range(1, K):
                            if arr[col+k][row] == 1:
                                word_count += 1
                            elif word_count == K:
                                count += 1
                                break
                        if word_count == K:
                            count += 1
            else:
                break

    return count

T = int(input())
for t in range(T):
    N, K = map(int, input().split())
    input_lst = [list(map(int, input().split()) + [0]) for _ in range(N) * [[0] * N]]
    print(f'#{t+1} {word_sapce_in_puzzle(input_lst, N, K)}')