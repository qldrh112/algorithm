import sys

sys.stdin = open('input.txt', 'r')


def solution(n, nums):
    max_v = 0 if nums[0] == (0 or 1) else 1  # 시작점이 0이면 1부터 시작, 그렇지 않으면 곱해야 하니까 1부터 시작
    for num in nums:
        if num == 0 or num == 1:
            max_v += num
        else:
            max_v *= num
    return max_v


if __name__ == '__main__':
    T = int(input())
    for x in range(T):
        N = int(input())
        input_list = list(map(int, input().rstrip().split()))
        print(f'#{x + 1} {solution(N, input_list)}')
