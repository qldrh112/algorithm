def solution(n, k, lst):
    """
    n: lst의 길이
    k: 넣을 성적의 수
    lst: 성적 목록
    """
    if n == k:
        return sum(lst)
    else:
        return sum(lst[:k])


T = int(input())
for t in range(T):
    N, K = map(int, input().split())
    input_lst = sorted(list(map(int, input().split())), reverse=True)
    print(f'#{t+1} {solution(N, K, input_lst)}')