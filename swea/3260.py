def solution(num1, num2):
    return num1 + num2

T = int(input())
for t in range(T):
    input_num1, input_num2 = map(int, input().split())
    print(f'#{t+1} {solution(input_num1, input_num2)}')