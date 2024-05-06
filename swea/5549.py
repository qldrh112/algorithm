def solution(string):
    odd = ['1', '3', '5', '7', '9']
    if string[-1] in odd:
        return 'Odd'
    else:
        return 'Even'


T = int(input())
for t in range(T):
    input_string = input()
    print(f'#{t+1} {solution(input_string)}')