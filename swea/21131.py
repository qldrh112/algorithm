import sys
sys.stdin = open('input.txt')

def solution(n, matrix):
    """
    메모리: 56,668 kb
    실행시간: 724 ms
    """
    """
    params: n -> int
    params: matrix -> List[List[int]]
    return: int
    """
    # 원래는 모든 matrix[i][i]와 모든 matrix의 성분을 전치했을 때 제 위치로 가는지 확인해야 하지만 문제에 불가능한 조건에 대한 언급이 없으니 그냥 진행한다.
    answer = 1
    # 1부터 n까지 세로 한 줄을 쭉 보면서 제 위치에 있는 것에 대한 리스트 생성
    collected = [True] + [False] * (n - 1)
    for i in range(1, n):
        if matrix[i][0] == i * n + 1:
            collected[i] = True

    # 시작점을 찾음, False가 없으면 전치할 필요가 없다.
    try:
        idx, value = n - 1 - collected[::-1].index(False), False
    except ValueError:
        return 0
    
    # n - 1부터 1까지 이동하며 T -> F, F -> T의 개수를 셈
    while idx > 1:
        idx -= 1
        if collected[idx] != value:
            value = not value
            answer += 1
    return answer


T = int(input())
for _ in range(T):
    N = int(input())
    input_arr = [list(map(int, input().split())) for _ in range(N)]
    print(solution(N, input_arr))