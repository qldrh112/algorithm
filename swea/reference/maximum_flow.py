import sys
sys.stdin = open('input.txt', 'r')
from collections import deque


def maximum_flow(source, sink, capacity):
    total_flow = 0
    #  흐름을 확인하는 현황판 제작
    flow = [[0] * V for _ in range(V)]


    while True:
        # 부모 정보를 담은 리스트로 추적
        parent = [-1] * V
        parent[source] = 0

        # 경로 탐색 
        q = deque([0])

        while q:
            here = q.popleft()
            for there in range(V):
                # 용량이 초과되지 않고, 연결이 되지 않았으면
                if capacity[here][there] - flow[here][there] > 0 and parent[there] == -1:
                    parent[there] = here
                    q.append(there) # 큐에 추가

                    if there == sink:
                        break   # for there in ~
        
        print(parent) 
        # 경로를 탐색할 수 없으면 중지
        if parent[sink] == -1:
            break   # while True
        
        # 경로를 다시 되돌아오며 가장 작은 값 찾기
        p = sink
        amount = float('inf')
        while p != source:
            amount = min(amount, capacity[parent[p]][p] - flow[parent[p]][p])
            p = parent[p]
        
        # flow에 반영하기
        p = sink
        while p != source:
            flow[parent[p]][p] += amount
            flow[p][parent[p]] -= amount
            p = parent[p]
        total_flow += amount

    return total_flow


T = int(input())
for t in range(T):
    V, E = map(int, input().split())
    capacity = [[0] * V for _ in range(V)]
    
    for _ in range(E):
        here, there, weight = map(int, input().split())
        capacity[here][there] = weight

    print(f'#{t + 1} {maximum_flow(0, V - 1, capacity)}')