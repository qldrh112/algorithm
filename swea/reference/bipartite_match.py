import sys
sys.stdin = open('input.txt', 'r')

def dfs(a):
    # 방문한 적이 있으면 실패
    if visited[a] == True:
        return False
    visited[a] = True   # 방문 기록하기
    
    # 연결할 수 있는 countB를 찾음
    for b in range(countB):
         # 연결이 되어 있고, 매칭이 되어 있지 않거나 재매칭 가능성 확인
        if adj[a][b] and (matchB[b] == -1 or dfs(matchB[b])):   # matchB[b] = 어떤 a값을 가지니까 현시점에서 이어질 수 있는 걸 찾을 수 있네
            matchA[a] = b
            matchB[b] = a
            return True
        
    return False    # 매칭을 찾지 못한 경우
        

def bipartite_march():
    result = 0
    for a in range(countA):
        if dfs(a):
            result += 1
    return result


T = int(input())
for t in range(T):
    countA = int(input())   # A그룹 맴버 수
    countB = int(input())   # B그룹 맴버 수
    adj = [[0] * countB for _ in range(countA)] # 연결을 표시하는 matrix
    # 연결을 만들어주다.
    N = int(input())    # 연결 선의 수
    for _ in range(N):
        a, b = map(int, input().split())
        adj[a - 1][b - 1] = 1
    visited = [False] * countA   # 방문 노드를 확인하는 배열
    matchA = [-1] * countA
    matchB = [-1] * countB
    print(f'#{t + 1} {bipartite_march()}')


