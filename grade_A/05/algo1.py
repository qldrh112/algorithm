"""
실행시간 : 50개의 테스트 케이스를 합쳐서 C/C++의 경우 3초, JAVA의 경우 3초, Python 10초

메 모 리 : Heap, Global, Stack 등을 모두 합해 최대 256MB까지 사용 가능 (단, 스택은 최대 1MB까지
"""
from heapq import heappush


def solution(villages, voter):
    def comb(n):
        hq = []
        for num in range(1, 2 ** n - 1):
            combine = [0] * n
            for k in range(n - 1, -1, -1):
                if num & 1:
                    combine[k] = 1
                num >>= 1

            area1 = sum([voter[x] for x in range(n) if combine[x] == 0])
            area2 = sum([voter[x] for x in range(n) if combine[x] == 1])
            diff = abs(area2 - area1)
            heappush(hq, (diff, combine))
        return hq

    def check(b1, b2):
        c1 = [x for x in range(N) if case[x] == 0]
        c2 = [x for x in range(N) if case[x] == 1]

        if len(c1) > 1:
            for p in c1:
                if p not in b1:
                    return False

        if len(c2) > 1:
            for q in c2:
                if q not in b2:
                    return False
        return True

    # 인접리스트 생성
    adj = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if villages[i][j] == 1:
                adj[j].append(i)

    # 후보군 생성
    candidate = comb(N)

    # 유효성 검증
    for value, case in candidate:
        a1, a2 = [], []
        for x in range(N):
            if case[x] == 0:
                a1.extend(adj[x])
            else:
                a2.extend(adj[x])
        if not check(a1, a2):
            continue
        else:
            return value


T = int(input())
for t in range(T):
    N = int(input())
    input_arr = [list(map(int, input().split())) for _ in range(N)]
    input_lst = list(map(int, input().split()))
    print(f'#{t+1} {solution(input_arr, input_lst)}')

