"""
메모리: 66,772 kb
실행시간: 201 ms
"""
def f(i, string):
    global lst, pointer

    if len(lst) == 8:
        return

    elif i > M - 8:
        return

    elif password_map.get(string[i:i + 7]) != None:
        if not lst:
            pointer = i + 1
        lst.append(password_map[string[i:i + 7]])
        f(i + 7, string)

    elif lst:
        lst = []
        f(pointer, string)

    else:
        f(i + 1, string)


def code(code_lst):
    tmp = 0
    for idx, value in enumerate(code_lst):
        if idx % 2:
            tmp += value
        else:
            tmp += 3 * value
    if tmp % 10:
        return 0
    else:
        return sum(code_lst)


password_map = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9,
}

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    flag = False
    for _ in range(N):
        input_lst = input()
        if flag:
            continue
        lst = []
        pointer = 0
        f(0, input_lst)
        if len(lst) == 8:
            result = code(lst)
            if result:
                flag = True
                print(f'#{t+1}', result)
    if not flag:
        print(f'#{t+1}', 0)
