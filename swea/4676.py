from collections import Counter


def solution(string, hyphen_num, counter):
    answer, prev = '', 0
    for idx in counter:
        answer += string[prev:idx] + '-' * counter[idx]
        prev = idx
    # 마지막 하이픈 이후의 문자열 붙이기
    answer += string[prev:]
    return answer


T = int(input())
for t in range(T):
    input_str = input()
    H = int(input())
    counter = Counter(list(map(int, input().split())))
    print(f'#{t+1} {solution(input_str, H, counter)}')

T = int(input())

for tc in range(1,T+1):
    s = list(input())
    print(s)
    h = int(input())
    arr = list(map(int,input().split()))
    arr.sort(reverse=True)
    for i in arr:
        s.insert(i,'-')

    print('#%d ' % tc,end='')
    print(*s,sep='')