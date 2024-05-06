def min_bill_charge(won):
    # bill: 지폐 항목
    # charges: 거스름돈 
    bill = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    charges = [0] * 8

    for i in range(8):
    # for문으로 변경하고, 앞에서부터 많은 지폐로 나누어 그 몫을 거스름돈으로
    # 이후 거슬러줄 돈을 거스름돈만큼 차감
        charges[i] = won // bill[i]
        won -= charges[i] * bill[i]
        
    return charges

T = int(input())
for t in range(T):
    won = int(input())
    print(f'#{t+1}')
    print(*min_bill_charge(won))