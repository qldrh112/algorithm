def solution(planted, watered):
    answer = []

    water_period = planted[:]
    watered = list(map(lambda x: x - 1, watered))
    n = len(planted)
    bad_mood = [False] * n

    for choice in watered:
        tmp = n
        # 식물을 순회하며 기분을 조정한다.
        for i in range(n):
            # 이미 기분이 좋지 않은 식물
            if bad_mood[i]:
                tmp -= 1
            # 지금 물을 준 식물
            elif i == choice:
                planted[i] = water_period[i]
            # 상해버린 식물
            elif planted[i] == 1:
                bad_mood[i] = True
                tmp -= 1
            else:
                planted[i] -= 1
        answer.append(tmp)

    return answer


print(solution([2, 1, 4, 3], [3, 1, 2, 1, 4, 4]))
print(solution([9, 4, 5, 5, 9, 1, 1, 6, 5, 4], [5, 3, 2, 6, 10, 7, 5, 10, 6, 5, 6, 10, 3, 9, 3, 4, 3, 2, 8, 9]))
print(solution([4, 7, 8, 4, 5, 6, 8, 10, 8, 9], [7, 3, 4, 10, 10, 9, 6, 3, 10, 3, 1, 3, 10, 2, 10, 1, 3, 10, 1, 9, 4, 4, 7, 10, 1, 2, 8, 8, 1, 3, 9, 3, 6, 3, 6, 6, 6, 7, 9, 10, 10, 9, 2, 3, 2, 1, 10, 8, 3, 10, 8, 8, 6, 5, 2, 4, 8, 6, 6, 10, 1, 2, 4, 6, 7, 5, 10, 7, 9, 5, 1, 7, 2, 4, 9, 7, 10, 5, 10, 7, 1, 5, 3, 9, 3, 3, 6, 2, 5, 2, 10, 10, 9, 9, 9, 10, 8, 8, 10, 2]))