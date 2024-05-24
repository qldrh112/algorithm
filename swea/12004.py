"""
메모리: 44,992 kb
실행시간: 160 ms
"""


def solution(num):
    # 1은 1과 1의 곱으로 표현
    if num == 1:
        return 'Yes'
    for a in range(2, 10):
        b, mod = divmod(num, a)
        # 나머지가 0이고, 몫이 10보다 작다면
        if not mod and b < 10:
            return 'Yes'
    return 'No'


TC = int(input())
for t in range(TC):
    N = int(input())
    print(f'#{t+1} {solution(N)}')