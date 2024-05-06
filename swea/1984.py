T = int(input())
for t in range(T):
    input_lst = list(map(int, input().split()))
    # [3, 17, 1, 39, 8, 41, 2, 32, 99, 2]

    input_lst.remove(max(input_lst))
    input_lst.remove(min(input_lst))

    # 여기서 문제, 소수점 첫째자리에서 반올림이 안 됨 ㅋㅋ

    print(f'#{t+1} {int(round(sum(input_lst)/len(input_lst), 0))}')