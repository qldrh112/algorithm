def frog_jump(lst):
    idx = lst[0]
    output = lst[idx]
    double = False
    boost = 0

    for _ in range(1, K):

        if 0 <= idx + lst[idx] + abs(boost) < N:

            if double and lst[idx] > 0:
                idx += lst[idx] + abs(boost)
                output += lst[idx]
                double = False

            elif double and lst[idx] <= 0:
                boost = lst[idx]
                idx += lst[idx]
                output += lst[idx]

            elif not double and lst[idx] > 0:
                idx += lst[idx]
                output += lst[idx]
                
            else:
                boost = lst[idx]
                idx += lst[idx]
                output += lst[idx]
                double = True

        else:
            return output
        
    return output

T = int(input())
for t in range(T):
    N, K = map(int, input().split())
    input_lst = list(map(int, input().split()))
    print(f'#{t+1} {frog_jump(input_lst)}')