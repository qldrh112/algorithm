import sys
sys.stdin = open('input.txt', 'r')


def solution(sequences, current=0 , wait=0, before=None):
    b_loc, o_loc = 1, 1
    
    for seq in sequences:
        color, target = seq[0], int(seq[1:])

        # 파란색 로봇
        if color == 'B':
            press_time = abs(target - b_loc) + 1
            
            # 이전 수행 로봇과 같다면
            if color == before:
                current += press_time
                wait += press_time
                b_loc = target
                before = 'B'

            # 이전 수행 로봇과 다르고 단추 누르는 시간이 대기 시간보다 길다면
            elif press_time > wait:
                current += (press_time - wait)
                wait = press_time - wait
                b_loc = target
                before = 'B'
            
            # 이전 수행 로봇과 다르고 단추 누르는 시간이 대기 시간보다 짧거나 같다면
            else:
                current += 1
                wait = 1
                b_loc = target
                before = 'B'
            
        # 주항색 로봇
        else:
            press_time = abs(target - o_loc) + 1
            
            # 이전 수행 로봇과 같다면
            if color == before:
                current += press_time
                wait += press_time
                o_loc = target
                before = 'O'

            # 이전 수행 로봇과 다르고 단추 누르는 시간이 대기 시간보다 길다면
            elif press_time > wait:
                current += (press_time - wait)
                wait = press_time - wait
                o_loc = target
                before = 'O'
            
            # 이전 수행 로봇과 다르고 단추 누르는 시간이 대기 시간보다 짧거나 같다면
            else:
                current += 1
                wait = 1
                o_loc = target
                before = 'O'

    return current

# 입력 처리 및 실행 부분
TC = int(input())
for t in range(TC):
    N, *input_list = input().split()
    sequences = [input_list[i] + input_list[i+1] for i in range(0, 2 * int(N), 2)]
    print(f'#{t+1} {solution(sequences)}')
