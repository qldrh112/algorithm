def close_0(num_list):
    """
    params num_list: 사람들의 비거리
    return: 0과 가장 가까운 거리의 절댓값
    """
    
    most_close_dist = 99999
    people = 1

    for num in num_list:
        # 0보다 클 때
        if num > 0 and (num < most_close_dist or num < (0 - most_close_dist)):
            most_close_dist = num
            people = 1
        # 0보다 작을 때
        elif num < 0 and (num < (0 - most_close_dist) or (0 - num) < most_close_dist):
            most_close_dist = num
            people = 1
        # num = most_close_dist
        elif num == most_close_dist or (0 - num) == most_close_dist or num == (0 - most_close_dist) or (0 - num) == (0 - most_close_dist):
            people += 1
    
    # 음수면 양수로 바꿉니다.
    if most_close_dist < 0:
        most_close_dist = 0 - most_close_dist

    return most_close_dist, people 

T = int(input())
for t in range(T):
    N = int(input())
    numbers = list(map(int, input().split()))
    # 출력합니다. '*'로 튜플도 풀 수 있다.
    print(f'#{t+1}', *close_0(numbers))