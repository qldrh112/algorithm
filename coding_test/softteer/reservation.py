import sys
sys.stdin = open('input.txt', 'r')
from heapq import heappush

def solution(requests):
    reservations = [(requests[0], requests[0] + 60)]
    answer = 1

    for start_time in requests[1:]:
        # 가장 이른 회의 시작 시간보다 일찍 마무리되거나 가장 늦은 회의 종료 시간 보다 늦게 시작하거나
        if start_time + 60 < reservations[0][0] or start_time > reservations[-1][1]:
            heappush(reservations, (start_time, start_time + 60))
            answer += 1
            continue
        
        for j, reservation in enumerate(reservations):
            use_time = reservation[0] - start_time
            # 30분 이상 회의 시간이 확보되면
            if use_time >= 30:
                # 가장 빠른 예약 시작 시각보다 이르면
                if j == 0:
                    heappush(reservations, (start_time, reservations[0][0] - 1))
                    answer += 1
                elif reservations[j - 1][1] < start_time:
                    heappush(reservations, (start_time, max(start_time + 60, reservations[j][0] - 1)))
                    answer += 1
    return answer

for _ in range(3):
    N = int(input())
    inputs = [input().split() for _ in range(N)]
    # Convert time to minutes
    requests = [(int(h) * 60 + int(m)) for h, m in inputs]
    print(solution(requests))
