def solution(horn, entity):
    twinhorn = horn - entity
    unicorn = entity - twinhorn
    return unicorn, twinhorn


T = int(input())
for t in range(T):
    # 뿔의 수 N, 짐승의 수 M
    N, M = map(int, input().split())
    # 유니콘 수, 트윈혼 수
    print(f'#{t+1}', *solution(N, M))