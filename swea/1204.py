def find_most_number(scores):
    """
    params scores: 학생들의 성적 리스트(list)
    return: 최빈수
    most_num: 최빈수
    max_v: 최빈수의 등장빈도
    total: 반복문을 다 돌지 않고 마무리할 수 있게
    """
    most_num = -1
    max_v = -1
    total = 1000

    for num in range(0, 100+1):
        if max_v <= scores.count(num):
            total -= scores.count(num)
            if total < max_v:
                return most_num
            most_num, max_v = num, scores.count(num)
    
    return most_num

T = int(input())
for t in range(T):
    tc = int(input())
    input_nums = list(map(int, input().split()))
    # 출력합니다.
    print(f'#{tc} {find_most_number(input_nums)}')