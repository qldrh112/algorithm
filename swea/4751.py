def solution(string):
    arr = [['.'] * n for _ in range(5)]
    for i in range(5):
        if i == 2:
            for j in range(0, n, 2):
                if j % 4:
                    arr[i][j] = string[j//4]
                else:
                    arr[i][j] = '#'
        elif i % 2:
            for j in range(1, n, 2):
                arr[i][j] = '#'
        else:
            for j in range(2, n, 4):
                arr[i][j] = '#'
    return arr


T = int(input())
for t in range(T):
    input_string = input()
    n = 4 * len(input_string) + 1
    answer = solution(input_string)
    for row in range(5):
        for col in range(n):
            if col < n-1:
                print(answer[row][col], end='')
            else:
                print(answer[row][col])
