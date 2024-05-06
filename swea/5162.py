def solution(bread1, bread2, budget):
    # 2번빵이 더 저렴하면
    if bread1 > bread2:
        if budget % bread2:
            answer = budget // bread2 + (budget % bread2) // bread1
        else:
            answer = budget // bread2
    # 1번빵이 더 저렴하거나 두 빵의 가격이 같으면
    else:
        if budget % bread1:
            answer = budget // bread1 + (budget % bread1) // bread2
        else:
            answer = budget // bread1
    return answer


T = int(input())
for t in range(T):
    A, B, C = map(int, input().split())
    print(f'#{t+1} {solution(A, B, C)}')