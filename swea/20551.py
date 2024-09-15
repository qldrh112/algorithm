def solution(num1, num2, num3):
    """
    메모리: 44,040 kb
    실행시간: 122 ms
    """
    if num2 < 2 or num3 < 3:
        return -1
    else:
        answer = 0
        eaten = compare_num(num2, num3)
        answer += eaten
        answer += compare_num(num1, num2 - eaten)
        return answer
    
def compare_num(small, big):
    return small - (big - 1) if small >= big else 0

T = int(input())
for t in range(T):
    A, B, C = map(int, input().split())
    print(f'#{t + 1} {solution(A, B, C)}')