def simple_factorization(num):
    """
    params num: 소인수분해하고자 하는 수
    return: 지수 리스트
    """
    # 밑 리스트와 지수 리스트는 1대1 관계
    # 밑 리스트
    base_lst = [2, 3, 5, 7, 11]
    # 지수 리스트
    exponent_lst = [0] * 5

    for i in range(4, -1, -1):
        count = 0
        # 숫자가 밑으로 나누어지면 count를 하나 추가하고, 숫자를 밑으로 나눕니다.
        while num % base_lst[i] == 0:
            count += 1
            num /= base_lst[i]

        exponent_lst[i] = count

    return exponent_lst

T = int(input())
for t in range(T):
    numbers = int(input())
    # 출력합니다.
    print(f'#{t+1}', *simple_factorization(numbers))