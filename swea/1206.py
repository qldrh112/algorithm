"""
메모리: 63,312 kb
실행시간: 198 ms
"""

def view_check(lst):
    cnt = 0
    # 건물이 있는 곳을 기준으로 2개 비워져 있으니 n-2
    for i in range(2, N-2):
        # 좌우 2개의 세대와의 높이 차 확인
        tmp = [lst[i] - lst[i + j] for j in [-2, -1, 1, 2] if lst[i] - lst[i + j] > 0]
        # 하나라도 음수면 다 쳐내라
        if len(tmp) == 4:
            cnt += min(tmp)
    return cnt


for t in range(1, 10+1):
    N = int(input())
    input_lst = list(map(int, input().split()))
    print(f'#{t} {view_check(input_lst)}')



def view_check(lst):
    """
    메모리: 63,044 kb
    실행시간: 197 ms
    """
    cnt = 0
    # 건물이 있는 곳을 기준으로 2개 비워져 있으니 n-2
    for i in range(2, N-2):
        # 최대 높이 255
        tmp = 255
        flag = True
        for j in [-2, -1, 1, 2]:
            tmp = min(tmp, lst[i] - lst[i+j])
            # 옆집 높이가 더 크거나 같으면
            if lst[i] - lst[i + j] <= 0:
                flag = False
                # for j
                break
        if flag:
            cnt += tmp
    return cnt


for t in range(1, 10+1):
    N = int(input())
    input_lst = list(map(int, input().split()))
    print(f'#{t} {view_check(input_lst)}')