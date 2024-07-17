import sys
sys.stdin = open('input.txt', 'r')

def solution(n, seq):
    output, min_v = 1, seq[-1]
    # 수열에서 뒷 숫자의 크기가 앞 숫자의 크기보다 크면 연속 가능
    # 수열의 크기가 5면 3번 인덱스부터 0번 인덱스까지 확인
    for i in range(n-2, -1, -1):
        if seq[i] < seq[i+1]:
            output += 1
            min_v = min(min_v, seq[i])

    return output


T = int(input())
for t in range(T):
    N = int(input())
    input_seq = list(map(int, input().split()))
    print(f'#{t+1} {solution(N, input_seq)}')