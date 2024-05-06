def solution(n, deck):
    answer = [0] * n
    left = 0
    if n % 2:
        right = n // 2 + 1
    else:
        right = n // 2

    for i in range(n):
        if i % 2:
            answer[i] = deck[right]
            right += 1
        else:
            answer[i] = deck[left]
            left += 1
    return answer


T = int(input())
for t in range(T):
    N = int(input())
    input_lst = list(input().split())
    print(f'#{t + 1}', *solution(N, input_lst))
