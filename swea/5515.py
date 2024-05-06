def solution(month, day):
    """
    2016/1/1 => 금
    월: 0, 화: 1, 수: 2, 목: 3, 금: 4, 토: 5, 일: 6
    """
    month_map = {
        1: 31,
        2: 29,
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
    days = sum([month_map[x] for x in range(1, month)]) + day
    # 1일(금요일)을 기준으로 주어진 값을 출력하기 위해선 3을 더하고 7을 나누어서 0~6까지 값 유지
    answer = (days % 7 + 3) % 7
    return answer


T = int(input())
for t in range(T):
    m, d = map(int, input().split())
    print(f'#{t+1} {solution(m, d)}')