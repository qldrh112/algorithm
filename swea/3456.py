def find_other_line(a, b, c):
    if a == b:
        return c
    elif a == c:
        return b
    else:
        return a


T = int(input())
for t in range(T):
    a, b, c = map(int, input().split())
    print(f'#{t+1} {find_other_line(a, b, c)}')