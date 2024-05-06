"""
메모리: 71,640 kb
실행시간: 1,291 ms
"""
def avg_score(scores):
    after_score = sum(list(map(lambda x: max(x, 40) // 5, scores)))
    return after_score


T = int(input())
for t in range(T):
    input_nums = list(map(int, input().split()))
    print(f'#{t+1} {avg_score(input_nums)}')