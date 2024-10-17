def solution(n, per, bread, arrives):
    """
메모리: 52,020 kb
실행시간: 509 ms
    """
    productions = [i // per * bread for i in range(arrives[-1] + 1)]
    for i, time in enumerate(arrives):
        if productions[time] - (i + 1) < 0:
            return 'Impossible'
    return 'Possible'

def solution(N, M, K, arrives):
    arrives.sort()  # 손님 도착 시간 정렬
    for i in range(N):
        # 현재 손님이 도착할 때까지 만들어진 붕어빵의 개수
        produced_bread = (arrives[i] // M) * K
        # 만약 현재까지 만들어진 붕어빵이 i+1번째 손님에게 충분하지 않으면 불가능
        if produced_bread < i + 1:
            return "Impossible"
    return "Possible"


T = int(input())
for x in range(T):
    N, M, K = map(int, input().split())
    input_list = list(map(int, input().split()))
    print(f'#{x + 1} {solution(N, M, K, sorted(input_list))}')