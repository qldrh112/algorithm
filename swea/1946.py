def unzip_alp(arr):
    """
    arr: [문자열, 숫자]로 입력된 2차원 리스트
    return: 압축해제한 내용
    """
    # cnt 가 10 이면 줄 바꿈
    cnt = 0
    for str, num in arr:
        for _ in range(int(num)):
            cnt += 1
            if cnt % 10 == 0:
                print(str)
            else:
                print(str, end='')
    # 다음 테스트 케이스 넘버와 겹치지 않게 하기 위해서
    print()

T = int(input())
for t in range(T):
    N = int(input())
    input_arr = [input().split() for _ in range(N)]
    # 출력합니다.
    print(f'#{t+1}')
    unzip_alp(input_arr)