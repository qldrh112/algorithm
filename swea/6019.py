import sys
sys.stdin = open('input.txt', 'r')

def solution(dist, a_speed, b_speed, fly_speed):
    answer = dist / (a_speed + b_speed) * fly_speed
    return answer 


T = int(input())
for t in range(T):
    D, A, B, F = map(int, input().split())
    print(f'#{t+1} {solution(D, A, B, F)}')