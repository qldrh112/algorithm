def racing_diff(nums):
    up, down = 0, 0
    for i in range(N-1):
        # 오르막길
        if nums[i+1] - nums[i] > 0:
            up = max(up, nums[i+1] - nums[i])
        # 내리막길
        elif nums[i+1] - nums[i] < 0:
            down = min(down, nums[i+1] - nums[i])

    return up, abs(down)


T = int(input())
for x in range(T):
    N = int(input())
    input_nums = list(map(int, input().split()))
    print(f'#{x+1}', *racing_difficult(input_nums))