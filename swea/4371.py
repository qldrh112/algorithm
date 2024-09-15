import sys
sys.stdin = open('input.txt', 'r')

def solution(n, days):
    """
    메모리: 52,072 kb
    실행시간: 305 ms
    """
    result, end_point = 0, days[-1]
    li = []

    for i in range(1, n):
        if i in li:
            continue    # for i
        else:
            diff = days[i] - days[0]
            idx, tmp = 0, []
            # 인덱스가 리스트를 초과하지 않으며 가장 큰 값보다 다음 값이 작다면 반복
            while idx < n - 1 and days[idx] + diff <= end_point:    
                try:
                    # idx: 1, 3, 4
                    idx = days.index(days[idx] + diff)
                    tmp.append(idx)
                except ValueError:
                    tmp.clear()
                    break   # while
            li.extend(tmp)
            result += 1 

    return result

T = int(input())
for t in range(T):
    N = int(input())
    days = [int(input()) for _ in range(N)]
    print(f'#{t + 1} {solution(N, days)}')