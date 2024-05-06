def solution(board):
    def dfs(i, level, col):
        # 마지막 행 도착
        if i == level:
            answer[0] += 1
            return
        # 모든 경우 판단
        else:
            for j in range(level):
                col[i] = j
                if promising(i, col):
                    dfs(i+1, level, col)

    def promising(i, col):
        """
        유효성 검증 함수
        """
        k, flag = 0, True
        while k < i and flag:
            # 행이 같거나 대각선으로 간섭받으면
            if col[k] == col[i] or col[k] + (i - k) == col[i] or col[k] - (i - k) == col[i]:
                flag = False
            k += 1
        return flag

    answer = [0]
    dfs(0, board, [-1] * board)
    return answer[0]


T = int(input())
for t in range(T):
    N = int(input())
    print(f'#{t + 1} {solution(N)}')