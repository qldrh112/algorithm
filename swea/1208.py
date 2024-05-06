"""
메모리: 61,468 kb
실행시간: 169 ms
"""
def flatten(dump, lst):
    lo, hi, do = 0, -1, 0

    # 변경 횟수가 주어진 것보다 작고, lo와 hi가 1 이상 차이가 난다면
    while do < dump and lst[lo] + 1 < lst[hi]:
        do += 1
        lst[hi] -= 1
        lst[lo] += 1

        i = 0
        while lst[lo+i] > lst[lo+i+1]:
            lst[lo+i], lst[lo+i+1] = lst[lo+i+1], lst[lo+i]
            i += 1

        i = 0
        while lst[hi+i] < lst[hi+i-1]:
            lst[hi+i], lst[hi+i-1] = lst[hi+i-1], lst[hi+i]
            i -= 1

    # 높의의 최고점과 최저점 반환
    return lst[hi] - lst[lo]


for t in range(1, 10+1):
    N = int(input())
    input_lst = sorted(list(map(int, input().split())))
    print(f'#{t} {flatten(N, input_lst)}')