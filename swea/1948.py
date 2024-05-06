def date_cal(past, future):
    """
    params: past: 과거 시간
    params: future: 미래 시간
    return: 미래와 과거의 차이(단위: 일)

    past[0]: 과거의 월
    past[1]: 과거의 일
    future[0]: 미래의 월
    future[1]: 미래의 일
    """
    month_day_dict = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31,
    }

    # 과거와 미래 사이에 있는 월의 목록
    full_day_month = [x for x in range(past[0] + 1, future[0])]

    # 과거의 월을 탈출하는 일 + 미래의 일 + 과거와 미래 사이의 일의 합
    if past[0] != future[0]:
        days = (month_day_dict[past[0]] - past[1]) + future[1] + sum([month_day_dict.get(x) for x in full_day_month])
    else:
        days = future[1] - past[1]

    # 시작 일자를 포함해야 하므로 +1을 더하여 반환한다.
    return days + 1

T = int(input())
for t in range(T):
    input_date = list(map(int, input().split()))
    print(f"#{t + 1} {date_cal(input_date[0:2], input_date[2:4])}")
