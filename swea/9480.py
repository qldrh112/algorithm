import sys
sys.stdin = open('input.txt', 'r')

def solution():
    

T = int(input())
for t in range(T):
    input_num1, input_num2 = map(int, input().split())
    print(f'#{t+1} {solution(input_num1, input_num2)}')