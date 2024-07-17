from collections import deque
# import sys
# sys.stdin = open('input.txt', 'r')

def check_space(spaces, pointer=0):
    flag = False
    for space in spaces:
        if spaces[space] == False:
            flag = True
            pointer = space
            return flag, pointer
    return flag, pointer

def order_adjustment(car, q):
    if car < 0:
        return car, q
    else:
        for idx, elem in enumerate(q):
            if elem < 0:
                q.appendleft(car)
                q[idx+1], car = 0, q[idx+1]
                return car, q
            
def solution(orders, spaces, cars, income=0):
    """
    메모리: 56,200 kb
    실행시간: 338 ms
    """
    while orders:
        # 다음 차가 들어갈 공간 확인
        has_space, pointer = check_space(spaces)

        car = order_q.popleft()
        # 공간이 없으면
        if not has_space:
            car, orders = order_adjustment(car, orders)

        # print(f'car: {car}')
        # print(f'orders: {orders}')
        # print(f'pointer: {pointer}')

        if car > 0:
            # 주차 위치와 차 정보 입력
            spaces[pointer] = car
            cars[car] = pointer
        elif car == 0:
            continue    # while
        else:
            car = abs(car)
            # 수입 계산
            income += R_i[cars[car]] * W_i[car-1]
            # 공간 확보
            spaces[cars[car]] = False

        # print(f'spaces: {spaces}')
        # print(f'cars: {cars}')
        # print(f'income: {income}')
        # print('-'* 50)
        
    return income


TC = int(input())
for t in range(TC):
    # n: 주차 공간, m: 차의 대수
    n, m = map(int, input().split())
    # 주차 자리 요금
    R_i = [int(input()) for _ in range(n)]
    # 차의 무게
    W_i = [int(input()) for _ in range(m)]

    order_q = deque([int(input()) for _ in range(m*2)])
    space_dict = {space: False for space in range(n)}
    car_dict = {car: False for car in range(1, m+1)}
    
    print(f'#{t+1} {solution(order_q, space_dict, car_dict)}')








# from collections import deque

# def check_space(spaces):
#     for i in range(len(spaces)):
#         if not spaces[i]:
#             return True, i
#     return False, -1

# def solution(orders, spaces, cars, R_i, W_i):
#     income = 0
#     wait_queue = deque()
#     n = len(spaces)

#     while orders:
#         car = orders.popleft()
#         if car > 0:  # 차가 들어오는 경우
#             has_space, pointer = check_space(spaces)
#             if has_space:
#                 spaces[pointer] = car
#                 cars[car] = pointer
#             else:
#                 wait_queue.append(car)
#         else:  # 차가 나가는 경우
#             car = abs(car)
#             income += R_i[cars[car]] * W_i[car-1]
#             spaces[cars[car]] = False
#             if wait_queue:
#                 next_car = wait_queue.popleft()
#                 spaces[cars[car]] = next_car
#                 cars[next_car] = cars[car]
#                 cars[car] = -1

#     return income

# TC = int(input())
# for t in range(TC):
#     n, m = map(int, input().split())
#     R_i = [int(input()) for _ in range(n)]
#     W_i = [int(input()) for _ in range(m)]
#     orders = deque([int(input()) for _ in range(m * 2)])
#     spaces = [False] * n
#     cars = [-1] * (m + 1)
    
#     print(f'#{t+1} {solution(orders, spaces, cars, R_i, W_i)}')