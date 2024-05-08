from collections import Counter
import sys
sys.stdin = open('algo1.txt')


def solution(n, trees):
    answer = 0
    trees = list(map(lambda x: x-trees[0], trees))[1:]
    counter = Counter(trees)
    print(counter)
    for num in counter:
        if num == 1:

    return answer



    # counter = Counter([trees[x][1] for x in range(n) if trees[x][1]])
    #
    # if counter[1] == counter[2]:
    #     answer += counter[1] * 2
    #     return answer
    #
    # elif counter[2] - counter[1] > 0:
    #     counter[2] -= counter[1]
    #
    # else:
    #     counter[1] -= counter[2]
    #     answer += counter[2] * 2 + counter[1] + (counter[1] - 1)
    #     return answer


T = int(input())
for t in range(T):
    N = int(input())
    input_lst = sorted(list(map(int, input().split())), reverse=True)
    print(f'#{t+1} {solution(N, input_lst)}')















# def solution(n, trees):
#
#
#     # 보기 좋게 처리
#     trees = list(map(lambda x: x - trees[-1], trees))
#     trees.pop()
#
#     # 나머지가 2라는 것은 홀수 일을 건너 뛰어야 함
#     if abs(sum(trees)) % 3 == 2:
#         answer = abs(sum(trees)) // 3 * 2 + 2
#     # 나머지가 1인 것은 홀수 일에 클리어 가능
#     elif abs(sum(trees)) % 3 == 1:
#         answer = abs(sum(trees)) // 3 * 2 + 1
#     # 딱 맞아 떨어짐
#     else:
#         answer = abs(sum(trees)) // 3 * 2
#
#     return answer
#
# T = int(input())
# for t in range(T):
#     N = int(input())
#     input_lst = sorted(list(map(int, input().split())))
#     print(f'#{t + 1} {solution(N, input_lst)}')