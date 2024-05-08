from collections import deque
"""
실행시간 : 50개의 테스트 케이스를 합쳐서 C/C++의 경우 3초, JAVA의 경우 3초, Python의 경우 10초

 

메 모 리 : Heap, Global, Stack 등을 모두 합해 최대 256MB까지 사용 가능 (단, 스택은 최대 1MB까지 사용 가능)
"""

def solution(arr):
    answer = 0
    visited = [-1] * 5

    def close_target_move(x, y):
        nonlocal answer, visited
        # 전체 보고 완료
        if visited == [-1] * 5:
            return
        # 보고해야 함
        elif 0 not in visited:
            target = close_target(x, y, 1)
            new_x, new_y = target
            visited[arr[x][y]] = -1
        # 사냥해야 함
        else:
            target = close_target(x, y, 2)
            new_x, new_y = target
            visited[arr[x][y]] = 1
        arr[new_x][new_y] = 0
        answer += (abs(x - new_x) + abs(y - new_y))
        close_target_move(new_x, new_y)

    def close_target(x, y, request):
        print(x, y, request)
        queue = deque([(x, y)])
        di = [0, 1, 1, 1, 0, -1, -1, -1]
        dj = [-1, -1, 0, 1, 1, 1, 0, -1]
        while queue:
            print(queue)
            x, y = queue.popleft()
            # 사냥
            if request == 2 and arr[x][y] > 0:
                return x, y
            # 보고
            elif request == 1 and arr[x][y] < 0:
                return x, y
            else:
                for k in range(8):
                    if 0 <= x + di[k] < N and 0 <= y + dj[k] < N:
                        queue.append((x + di[k], y + dj[k]))

    # 방문 리스트 만들기
    for row in range(N):
        for col in range(N):
            if arr[row][col] > 0:
                visited[arr[row][col]] = 0
    close_target_move(0, 0)

    return answer


T = int(input())
for t in range(T):
    N = int(input())
    input_arr = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{t+1} {solution(input_arr)}')