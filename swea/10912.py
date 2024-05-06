from collections import Counter


def solution(string):
    answer = ''
    counter = Counter(string)
    # 사전 순으로 정렬된 카운터에서 짝지어지지 않는 문자 탐색
    for char in sorted(counter):
        if counter[char] % 2:
            answer += char

    return answer if answer else 'Good'


T = int(input())
for t in range(T):
    input_string = input()
    print(f'#{t + 1} {solution(input_string)}')
