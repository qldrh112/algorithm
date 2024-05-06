def solution(k, scores, m):
    """
    k: 내 점수
    scores: 다른 사람의 점수
    m: 목표 점수
    """
    # [95, 90, 80, 80, 80, 70, 70, 70, 30, 10]
    # [25, 20, 10, 10, 10, 0, 0, 0, -40, -60]

    answer = 0
    n = len(scores)
    scores = list(map(lambda x: x - k, scores))
    start = len([x for x in range(len(scores)) if scores[x] > 0]) - 1
    obj = start - m + 2
    answer += obj
    rear = -1

    if start == n - 1 and m < n - 1:
        answer = -1

    else:
        while start >= m - 1:

            # 옮겨야 하는 놈이 더 작으면
            if scores[start] <= abs(scores[rear]):
                scores[rear] += scores[start]
                scores[start] = 0
                start -= 1

            # 옮겨야 하는 놈이 더 크고, 분배할 녀석이 있으면
            elif scores[rear] < 0:
                scores[start] -= abs(scores[rear])
                scores[rear] = 0
                rear -= 1
                answer += 1

            # 더 이상 분배할 수 없으면
            else:
                answer = -1
                break
    return answer + 1


print(solution(70, [95, 90, 80, 80, 80, 70, 70, 70, 30, 10], 4))
print(solution(1996, [2000, 1999, 1999, 1997], 3))
print(solution(65, [76, 76, 74, 72, 71, 69, 67, 62, 61, 60, 60, 59, 58], 3))