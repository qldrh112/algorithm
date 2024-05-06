def solution(length, haystack):
    """
    평균과의 편차만큼 건초더미를 옮겨야 함
    """
    target = sum(haystack) // length
    pretreatment_list = list(map(lambda x: x - target, haystack))
    answer = sum([x for x in pretreatment_list if x > 0])
    return answer


T = int(input())
for t in range(T):
    N = int(input())
    input_nums = [int(input()) for _ in range(N)]
    print(f'#{t+1} {solution(N, input_nums)}')