"""
메모리: 71,168 kb
실행시간: 357 ms
"""
def dont_homework_student(clear_student):
    return [x for x in range(1, N+1) if x not in clear_student]


T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    if N == K:
        print(f'#{tc+1}')
    else:
        input_lst = list(map(int, input().split()))
        print(f'#{tc+1}', *dont_homework_student(input_lst))