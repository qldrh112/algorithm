# 테스트 케이스 입력
T = int(input())
# T번 반복
for t in range(T):
    # 입력값
    N = int(input())
    total = 0
    # range(1, N+1)
    for i in range(1, N+1):
        if i % 2 == 1:
            total += i
        else:
            total -= i
    print(f'#{t+1} {total}')