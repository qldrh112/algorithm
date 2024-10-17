import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

def topological_sorting():
    # 1학기부터 시작이니까
    result = 1

    # 진입 차수가 0인 node(나를 참조하는 개수)를 큐에 추가하기
    queue = deque([(i, result) for i, node in enumerate(indegree) if node == 0 and i > 0])

    while queue:
        node, semester = queue.popleft()
        # 몇 번째 학기 수업이냐
        result = max(result, semester)

        # 진입 차수가 0인 노드를 큐에 추가하기
        for n in gragh[node]:
            # 수강한 과목의 상위 과목의 참조 개수 줄이기
            indegree[n] -= 1
            if indegree[n] == 0:
                queue.append((n, semester + 1))

    # 목적지에 도달할 수 없으면 발생하면 -1 반환
    if indegree[D]:
        return -1
    
    return result


T = int(input())
for t in range(T):
    V, E  = map(int, input().split())   # 정점, 간선
    D = int(input())    # 목적지
    
    # 그래프와 진입 차수를 만들고, 선후 관계 정리하기
    gragh = [[] for _ in range(V + 1)]
    indegree = [0] * (V + 1)

    for _ in range(E):
        start, end = map(int, input().split())
        gragh[start].append(end)
        indegree[end] += 1

    print(f'#{t + 1} {topological_sorting()}')