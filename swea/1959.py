def max_multiple_block(short_len, long_len, short, long):
    """
    param short_len: 짧은 리스트의 길이
    param long_len: 긴 리스트의 길이
    param short: 짧은 리스트
    param long: 긴 리스트
    return: 곱의 최고 값
    """
    max_v = 0

    # a와 b 중 뭐가 더 긴지 모르니 이런 코드를 작성해놓는다.    
    if short_len > long_len:
        short_len, long_len = long_len, short_len
        short, long = long, short

    for i in range(long_len-short_len+1):
        sum_product = 0
        for j in range(short_len):
            # 맞은편 녀석과 곱하기
            sum_product += short[j] * long[i+j]
        
        # 갱신
        if max_v < sum_product:
            max_v = sum_product

    return max_v


T = int(input())
for t in range(T):
    m, n = map(int, input().split())
    input1 = list(map(int, input().split()))
    input2 = list(map(int, input().split()))
    # 출력합니다.
    print(f'#{t+1} {max_multiple_block(m, n, input1, input2)}')