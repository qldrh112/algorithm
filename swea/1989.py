TC = int(input())

# N번만큼 반복합니다.
for N in range(TC):
    palindrome = input()
    discrimination = ''

    # 문자열의 중앙값-1만큼 반복합니다.
    for i in range(1, len(palindrome)//2+1):
        if palindrome[i-1] == palindrome[0-i]:
            discrimination = True

        # 같지 않으면 출력 후 종료
        else:
            discrimination = False
            print(f'#{N+1} 0')
            break
        
    if discrimination == True:
        print(f'#{N+1} 1')