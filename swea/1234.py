"""
메모리: 58,248 kb
실행시간:145 ms
"""
def search_password(n, nums):
    """
    params n(int): 문자열의 길이
    params: nums(str): 암호
    """
    stack = []
    for i in range(n):
        # 스택이 비어있을 때
        if not stack:
            stack.append(nums[i])
        # 스택의 마지막과 같을 때
        elif stack[-1] == nums[i]:
            stack.pop()
        # 스택의 마지막과 같지 않을 때
        else:
            stack.append(nums[i])

    return stack


for t in range(1, 10+1):
    N, input_nums = input().split()
    print(f'#{t}', ''.join(search_password(int(N), input_nums)))