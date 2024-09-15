import sys
sys.stdin = open('input.txt', 'r')

def solution(string):
    """
    메모리: 47,888 kb
    실행시간: 129 ms
    """
    people, result = 0, 0
    for i in range(len(string)):
        slaped = int(string[i])
        if people >= i:
            people += slaped
        else:
            result += 1
            people += slaped + 1
    return result

T = int(input())
for t in range(T):
    input_string = input()
    print(f'#{t + 1} {solution(input_string)}')