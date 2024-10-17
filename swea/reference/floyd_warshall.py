import sys
sys.stdin = open('input.txt', 'r')

def floyd_warshall(graph):
    # 인접점을 거치는 이동 경로 중에 최소 경로가 있다면 그것으로 변경
    for k in range(1, len(graph)):
        # 출발점
        for i in range(1, len(graph)):
            # 도착점
            for j in range(1, len(graph)):
                # i와 j가 같으면 최단 거리는 0
                if i == j:
                    graph[i][j] = 0
                    continue
                # i -> k -> j가 i -> j보다 이동을 덜하면
                elif graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
    return graph



T = int(input())
for t in range(T):
    N = int(input())
    M = int(input())

    # 인접 행렬을 만듦
    graph = [[float('inf')] * (N + 1) for _ in range(N + 1)]
    for _ in range(M):
        s, e, w = map(int, input().split())
        graph[s][e] = w
    
    graph = floyd_warshall(graph)
    print(f'#{t + 1}')
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if j == N:
                print(graph[i][j])
            else:
                print(graph[i][j], end=' ')

                
