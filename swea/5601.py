"""
메모리: 46,692 kb
실행시간: 111 ms
"""
def div_juice(N):
    return ['1/'+str(N)] * N


T = int(input())
for t in range(T):
    N = int(input())
    print(f'#{t+1}', *div_juice(N))