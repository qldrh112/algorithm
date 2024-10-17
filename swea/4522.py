import sys

sys.stdin = open('input.txt', 'r')


def solution(string):
    for i in range(len(string) // 2):
        # 대응되는 값이 값거나 ?가 들어가 있으면
        if string[i] == string[-1-i] or string[i] == '?' or string[-1-i] == '?':
            continue
        else:
            return 'Not exist'
    return 'Exist'


if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        input_string = input()
        print(f'#{t + 1} {solution(input_string)}')