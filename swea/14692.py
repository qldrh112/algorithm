"""
메모리: 44,984 kb
실행시간: 103 ms
"""


def solution(length):
    if length % 2:
        return 'Bob'
    else:
        return 'Alice'


T = int(input())
for t in range(T):
    input_num = int(input())
    print(f'#{t+1} {solution(input_num)}')