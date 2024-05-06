def water_bill(p, q, r, s, w):
    """
    p: A사의 1L 당 요금(int)
    q: B사의 rL이하 요금(int)
    r: q의 기준 사용량(int)
    s: B사의 1L당 추가 사용료(int)
    w: 실제 사용량(int)
    return: 내야하는 가장 최소 요금
    """
    # B사의 기본 요금 기준보다 적게 사용했으며
    if w <= r:
        # A사 요금이 더 적으면
        if q > p * w: 
            return p * w
        # B사 요금이 더 적으면
        else:
            return q
    
    # B사의 기본 요금 기준보다 많이 사용했으며
    else:
        # A사 요금이 더 적으면
        if q + (w - r) * s >= p * w:
            return p * w
        # B사 요금이 더 적으면 
        else:
            return q + (w - r) * s

T = int(input())
for t in range(T):
    P, Q, R, S, W = map(int, input().split())
    print(f'#{t+1} {water_bill(P, Q, R, S, W)}')