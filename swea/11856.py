from collections import Counter


def solution(string):
    counter = Counter(string)
    # EEEL 이걸 거를 수 있는 조건문
    if len(counter.keys()) == 2 and 2 in counter.values():
        return 'Yes'
    else:
        return 'No'


T = int(input())
for t in range(T):
    input_string = input()
    print(f'#{t+1} {solution(input_string)}')