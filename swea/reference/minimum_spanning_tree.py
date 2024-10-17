import sys
sys.stdin = open('input.txt', 'r')

import heapq as hq

def prim_mst():
    # 전체 거리
    total_weight = 0

    queue = [(0, 0)]    # 거리, 정점
    visited = [False] * (V + 1) # 방문 여부 추적

    while queue:
        # 요소를 꺼내어 전체 값에 추가하고, 방문 기록 남기기
        dist, node = hq.heappop(queue)
        visited[node] = True
        total_weight += dist

        for v in range(V):
            if not visited[v] and graph[dist][v] > 0:
                hq.heappush((graph[dist][v], v))



    return



T, V = map(int, input())
for t in range(T):
    graph = [list(map(int, input().split())) for _ in range(V + 1)]
    print(f'#{t + 1} {prim_mst()}')