"""
메모리: 62,332 kb
실행시간: 220 ms
"""
from collections import Counter


def align_numbers_sort():
    align_numbers = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    for i in range(10):
        # 외계어 사이에 공백 + 외계어가 바뀔 때 줄바꿈 X
        print((align_numbers[i] + ' ') * c[align_numbers[i]], end='')

    print()


T = int(input())
for _ in range(T):
    t, N = input().split()
    c = Counter(input().split())
    print(t)
    align_numbers_sort()