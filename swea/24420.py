import sys
sys.stdin = open("input.txt", "r")

def check_subset(set_a: set, set_b: set):
    """
        -  ‘=’: 두 집합 A와 B가 서로 같다.
        -  ‘<’: A와 B는 서로 다르고, A가 B의 부분집합이다.
        -  ‘>’: A와 B는 서로 다르고, B가 A의 부분집합이다.
        -  ‘?’: 위의 세 분류에 모두 해당하지 않는다.
    """
    # a_diff_b, b_diff_a = set_a - set_b, set_b - set_a

    # if a_diff_b == set():   # a - b가 공집합이면
    #     if b_diff_a == set():   # b - a도 공집합이면
    #         return '='
    #     else:   # b - a가 공집합이 아니면 b가 더 큰 놈
    #         return '<'
    # else:   # a - b가 공집합이 아니면
    #     if b_diff_a != set():   # b - a도 공집합이 아니면 부분집합 관계 없음
    #         return '?'
    #     else:   # b - a가 공집합이면 a가 더 큰 놈
    #         return '>'

    is_subsets = (set_a.issubset(set_b), set_b.issubset(set_a))

    if is_subsets == (True, True):
        return '='
    elif is_subsets == (True, False):
        return '<'
    elif is_subsets == (False, True):
        return '>'
    else:
        return '?'
    
T = int(input())
for t in range(T):
    len_input1, len_input2 = map(int, input().split())
    input1 = set(map(int, input().split()))
    input2 = set(map(int, input().split()))
    print(check_subset(input1, input2))

    
    

