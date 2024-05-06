from collections import Counter


def solution(string):
    counter = Counter(string.replace('()', '('))
    answer = counter['('] + counter[')']
    return answer


T = int(input())
for t in range(T):
    input_string = input()
    print(f'#{t+1} {solution(input_string)}')