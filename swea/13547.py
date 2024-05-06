def solution(process):
    if process.count('x') > 7:
        return 'NO'
    else:
        return 'YES'


T = int(input())
for t in range(T):
    input_string = input()
    print(f'#{t+1} {solution(input_string)}')