def solution(n, nums):
    answer, left = 0, nums[0]
    for i in range(1, n-1):
        if left < nums[i] < nums[i+1] or left > nums[i] > nums[i+1]:
            answer += 1
        left = nums[i]

    return answer


T = int(input())
for t in range(T):
    N = int(input())
    input_nums = list(map(int, input().split()))
    print(f'#{t+1} {solution(N, input_nums)}')