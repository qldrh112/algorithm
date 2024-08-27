def solution(a, b):
    """
    메모리: 52,572 kb
    실행시간: 686 ms
    """
    return (max(a, b) // min(a, b)) ** 2   

T = int(input())
for t in range(T):
    A, B = map(int, input().split())
    print(f'#{t+1} {solution(A, B)}')