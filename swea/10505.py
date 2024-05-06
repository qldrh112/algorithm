"""
메모리: 62,800 kb
실행시간: 227 ms
"""
def below_median_income(incomes):
    return len([income for income in incomes if avg >= income])


T = int(input())
for x in range(T):
    N = int(input())
    input_lst = list(map(int, input().split()))
    avg = sum(input_lst) / N
    print(f'#{x+1} {below_median_income(input_lst)}')