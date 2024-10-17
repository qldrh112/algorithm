import sys
sys.stdin = open('input.txt', 'r')

import heapq

def dijkstra(graph, start, end):
    dist = [float('inf')] * (V + 1)

    pq = [(0, start)]   # (비용, 위치)

    while pq:
        cost, here = heapq.heappop(pq)  # 현재 위치 기준


        # 만약 비용이 기존의 최소값보다 크다면 생략
        if cost > dist[here]:
            continue

        # 이웃 노드의 거리 갱신
        for neighbor, weight in graph[here]:
            next_dist = cost + weight

            # 이웃 노드로 이동하는 더 짧은 길을 발견하면 갱신 & 힙큐에 추가
            if dist[neighbor] > next_dist:
                dist[neighbor] = next_dist
                heapq.heappush(pq, (next_dist, neighbor))

    return dist[end]


T = int(input())
for t in range(T):
    V, START, END = map(int, input().split())    # 정점의 개수, 시작 정점, 도착 정점
    graph = [[] for _ in range(V + 1)]
    E = int(input())    # 간선 개수

    for _ in range(E):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))

    print(dijkstra(graph, START, END))    