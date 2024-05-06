def add_time(lst):

    hour = sum(lst[0:3:2])
    minute = sum(lst[1:4:2])

    if minute > 59:
        minute -= 60
        hour += 1
    
    if hour > 12:
        hour -= 12
    
    return hour, minute

T = int(input())
for t in range(T):
    input_lst = list(map(int, input().split()))
    # 이거 언패킹 안 하고 한 번에 출력할 수 있는 방법이 있나?
    hour, minute = add_time(input_lst)
    print(f'#{t+1} {hour} {minute}')