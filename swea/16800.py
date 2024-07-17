import sys
import math

sys.stdin = open('input.txt', 'r')

def solution(limit):
    """
    메모리: 48,168 kb
    실행시간: 707 ms
    """
    output = limit - 1
    for num in range(2, int(math.sqrt(limit))+1):
        div, mod = divmod(limit, num)
        cand = div + num - 2
        if not mod and output > cand:
            # print(div, mod)
            output = cand
    return output


TC = int(input())
for t in range(TC):
    N = int(input())
    print(f'#{t+1} {solution(N)}')