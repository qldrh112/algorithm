"""
메모리: 58,772 kb
실행시간: 168 ms
"""
def parallenlogram_max_size():
    return N ** 2


TC = int(input())
for t in range(TC):
    N = int(input())
    print(f'#{t+1} {parallenlogram_max_size()}')