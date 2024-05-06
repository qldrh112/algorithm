# 테스트 케이스의 수를 입력받습니다. 
T = int(input())
for i in range(T):
    # 테스트 케이스를 입력받습니다.
    TC = input()
    # 1부터 마디가 구성되어 있는지 확인합니다.
    for j in range(1, 10):
        if TC[0:j] == TC[0+j:j+j]:
            # 마디가 검출되면 종료합니다.
            print(f'#{i+1} {j}')
            break
