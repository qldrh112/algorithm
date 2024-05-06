# def profit_rule(list):
    
#     if len(list) == 0:
#         return 0
    
#     big_number_index = list.index(max(list)) 
    
#     if big_number_index == 0:
#         del list[0]
#         return profit_rule(list)
    
#     elif big_number_index == len(list)-1: 
#         output = 0
#         for i in range(len(list)-1):
#             output += max(list) - list[i]
#         return output 
    
#     else:
#         list1 = list[:big_number_index+1]  # [10, 5, 4, 8, 12]
#         list2 = list[big_number_index+1:]  # [1, 3, 5], [0]
#         return profit_rule(list1) + profit_rule(list2)
    
# T = int(input()) 
# for i in range(T):
#     N = int(input()) 
#     input_list = list(map(int, input().split())) # [10, 5, 4, 8, 12, 1, 3, 5, 0]
#     print(f'#{i+1}', profit_rule(input_list)) 


# def max_profit(days, prices):
#     """
#     days: 미래예지한 일(int)
#     prices: 일자별 가격(list)
#     profit: 최대 이익
#     top: 재원을 매도할 날짜 인덱스
#     checker: 재원을 매수할 날짜 인덱스
#     """
#     profit = 0
#     top = -1
#     checker = -2

#     for _ in range(days-1):
#         if prices[top] > prices[checker]:
#             profit += prices[top] - prices[checker]
#             checker -= 1
#         else:
#             top = checker
#             checker -= 1

#     return profit

# T = int(input())
# for t in range(T):
#     N = int(input())
#     input_list = list(map(int, input().split()))
#     print(f'#{t+1} {max_profit(N, input_list)}')



def max_profit(days, prices):
    """
    days: 미래예지한 일(int)
    prices: 일자별 가격(list)
    profit: 최대 이익
    top: 재원을 매도할 날짜 인덱스
    checker: 재원을 매수할 날짜 인덱스
    """
    profit = 0
    top = -1
    checker = -2

    for _ in range(days-1):
        if prices[top] > prices[checker]:
            profit += prices[top] - prices[checker]
            checker -= 1
        else:
            top = checker
            checker -= 1

    return profit

T = int(input())
for t in range(T):
    N = int(input())
    input_list = list(map(int, input().split()))
    print(f'#{t+1} {max_profit(N, input_list)}')