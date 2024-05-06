# 369 게임의 마지막 숫자
N = int(input())
three_six_nine = ['3','6','9']

# 1부터 N까지 반복합니다.
for i in range(1, N+1):
    # 받은 숫자를 문자형으로 변환합니다.
    str_N = str(i)
    tmp = 0 #369가 나온 횟수
    
    for j in range(len(str_N)):
        # 문자열의 요소 하나하나를 받아서 369가 있는지 확인합니다.
        if str_N[j] in a:
            tmp += 1
            
    # i에서 369가 나오는 횟수만큼 *를 반복합니다.
    if k != 0:
        print('-'*tmp, end=' ')
    else:
        print(i, end=' ')
        
