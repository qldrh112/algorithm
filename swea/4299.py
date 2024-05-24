"""
메모리: 44,728 kb
실행시간: 100 ms
"""


def solution(day, hour, minute):
    answer = 0

    # day
    if day >= 0:
        answer += day * 60 * 24
    else:
        return -1

    # hour
    if hour - 11 >= 0:
        answer += hour * 60
    # 11시보다 작으면
    else:
        answer += (hour + 24) * 60
        # day 내림으로 인해 시간이 0보다 줄어들면
        if answer - 60 * 24 < 0:
            return -1
        else:
            answer -= 60 * 24

    # minute
    if minute >= 0:
        answer += minute
    else:
        answer += minute + 60
        # 내림으로 인해 시간이 0보다 줄어들면
        if answer - 60 < 0:
            return -1
        else:
            answer -= 60

    return answer


T = int(input())
for t in range(T):
    D, H, M = map(int, input().split())
    print(f'#{t + 1} {solution(D - 11, H - 11, M - 11)}')


# def solution(day, hour, minute):
#     # 모든 시간을 분으로 변환
#     total_minutes = day * 24 * 60 + hour * 60 + minute
#     # 기준 시간인 11일 11시 11분을 뺌
#     diff = total_minutes - (11 * 24 * 60 + 11 * 60 + 11)
#     # 시간이 이전이면 -1 반환, 아니면 diff 반환
#     return -1 if diff < 0 else diff
#
#
# T = int(input())
# for t in range(T):
#     D, H, M = map(int, input().split())
#     print(f'#{t + 1} {solution(D, H, M)}')