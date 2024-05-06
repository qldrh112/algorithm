def rccar_move_meter(commands):
    """
    params n: command의 수
    params arr: [[command, accelation]]의 이차원 리스트
    return: rc카가 이동한 거리
    """
    rc_car = 0
    speed = 0

    for command in commands:
        # [0]
        if command[0] == 0:
            rc_car += speed
        # [1, @]
        elif command[0] == 1:
            speed += command[1]
            rc_car += speed
        # [0, @]
        elif speed - command[1] > 0 and command[0] == 2:
            speed -= command[1]
            rc_car += speed 
        else:
            speed = 0

    return rc_car

T = int(input())
for t in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 출력합니다.
    print(f'#{t+1} {rccar_move_meter(arr)}')