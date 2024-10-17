import sys
sys.stdin = open('input.txt', 'r')

def solution(bus_paths, num_of_stop, bus_stops):
    """
    메모리: 51,408 kb
    실행시간: 203 ms
    """
    """
    bus_paths - list(list(int)) : 버스 노선
    num_of_stop - int : 버스 정류장 수
    bus_stops - list(int) : 버스 정류장 목록
    return - list(int) : 각 버스 정류장을 지나는 버스의 수
    """
    bus_paths.sort(key=lambda x: x[0])
    answer = [0] * num_of_stop
    for path in bus_paths:
        for i in range(num_of_stop):
            if path[0] <= bus_stops[i] <= path[1]:
                answer[i] += 1
    return answer

T = int(input())
for x in range(T):
    N = int(input())
    input_arr = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    input_list = [int(input()) for _ in range(P)]
    print(f'#{x + 1}', *solution(input_arr, P, input_list))


# def solution(bus_paths, num_of_stop, bus_stops):
#     # 1에서 5000까지의 정류장에 대한 누적합 배열
#     bus_count = [0] * 5001

#     # 각 노선의 시작점에서 +1, 끝나는 지점 다음에서 -1
#     for path in bus_paths:
#         start, end = path
#         bus_count[start] += 1
#         if end + 1 <= 5000:
#             bus_count[end + 1] -= 1
    
#     # 구간 누적합을 계산하여 각 정류장을 지나는 버스 수 구하기
#     for i in range(1, 5001):
#         bus_count[i] += bus_count[i - 1]

#     # 필요한 버스 정류장에 대한 결과 추출
#     answer = [bus_count[stop] for stop in bus_stops]
#     return answer

# T = int(input())
# for x in range(T):
#     N = int(input())
#     input_arr = [list(map(int, input().split())) for _ in range(N)]
#     P = int(input())
#     input_list = [int(input()) for _ in range(P)]
#     print(f'#{x + 1}', *solution(input_arr, P, input_list))
