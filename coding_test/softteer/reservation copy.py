import sys
sys.stdin = open('input.txt', 'r')
from heapq import heappush, heappop

def solution(requests):

    # 우선순위 큐 (min-heap)
    reservations = []

    # 첫 회의는 무조건 예약
    heappush(reservations, (requests[0] + 60, requests[0]))
    count = 1

    for start_time in requests[1:]:
        # 가장 빨리 끝나는 회의의 끝나는 시간
        earliest_end_time = reservations[0][0]

        if start_time >= earliest_end_time:
            # 현재 회의가 끝난 후 회의를 시작할 수 있는 경우
            heappop(reservations)
            heappush(reservations, (start_time + 60, start_time))
            count += 1
        elif start_time + 60 <= earliest_end_time and start_time + 60 - start_time >= 30:
            # 회의를 새로 시작할 수 있는 경우
            heappush(reservations, (start_time + 60, start_time))
            count += 1

    return count

for _ in range(3):
    N = int(input())
    inputs = [input().split() for _ in range(N)]
    # Convert time to minutes
    requests = [(int(h) * 60 + int(m)) for h, m in inputs]
    print(solution(requests))
