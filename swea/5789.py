def solution(num_box, change_index, changes):
    """
    params num_box[int]: 상자의 수
    params change_index[int]: 변경 수
    params changes[list(list(int)): 변경점
    return[list(int)]: 규칙 적용 시 상자

    변경 내용을 거꾸로 타고 올라가서 이후의 변경된 상자는 다시 변경하지 않음
    """
    answer = [0] * num_box
    changed = {x: False for x in range(1, num_box+1)}
    # 모든 상자를 변경했거나 모든 변경 내용을 적용했다면
    while False not in changed.values() or change_index > 0:
        # 상자는 1번부터 시작하므로 left 는 하나 감소하여 적용
        left, right = changes[change_index-1][0] - 1, changes[change_index-1][1]
        for i in range(left, right):
            # 변경 여부에 따름
            if changed.get(i):
                continue
            else:
                answer[i] = change_index
                changed[i] = True
        change_index -= 1
    return answer


T = int(input())
for t in range(T):
    N, Q = map(int, input().split())
    input_arr = [list(map(int, input().split())) for _ in range(Q)]
    print(f'#{t+1}', *solution(N, Q, input_arr))