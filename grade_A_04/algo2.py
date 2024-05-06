import sys

sys.stdin = open('algo2.txt')


def solution(matrix):
    def col_check(i):
        max_v = 0
        for key, values in house_map.items():
            for v in values:
                for j in range(W):
                    if v == j:
                        max_v = max(max_v, abs(key - i))
                        # for j
                        break
        return max_v

    def row_check(i):
        max_v = 0
        for key, values in house_map.items():
            for j in range(H):
                if key == j:
                    for v in values:
                        max_v = max(max_v, abs(v - i))
                    # for j
                    break
        return max_v

    def left_diag_check(i, j):
        max_v = 0
        while j >= 0 and i < H:
            for v in house_map[i]:
                dist = abs(v - j)
                if dist == 0:
                    return 2500
                else:
                    max_v = max(max_v, dist)
                    print(i, j, v, max_v)
            i += 1
            j -= 1

        return max_v

    def right_diag_check(i, j):
        max_v = 0
        while j <= W - 1 and i < H:
            for v in house_map[i]:
                dist = abs(v - j)
                if dist == 0:
                    return 2500
                else:
                    max_v = max(max_v, dist)
            i += 1
            j += 1
        return max_v

    house_map = {}
    answer = 2500

    # 집의 위치를 딕셔너리로
    for row in range(H):
        tmp = []
        for col in range(W):
            if matrix[row][col] == '1':
                tmp.append(col)
        house_map[row] = tmp

    for row in range(H):
        for col in range(W):
            if matrix[row][col] == '0':
                # 행 검정
                if col == 0 and house_map[row] == []:
                    answer = min(answer, col_check(row))

                # 열 검정
                if row == 0 and col not in [x for lst in house_map.values() for x in lst]:
                    answer = min(answer, row_check(col))

                # 좌 대각 검정
                if col == W - 1 or (col != 0 and row == 0):
                    answer = min(answer, left_diag_check(row, col))
                    print(answer)

                # 우 대각 검정
                if col == 0 or (col != W - 1 and row == 0):
                    answer = min(answer, right_diag_check(row, col))

    if answer == 2500:
        return -1

    return answer


T = int(input())
for t in range(T):
    # w: 너비, h: 높이
    W, H = map(int, input().split())
    input_matrix = [input().split() for _ in range(H)]
    print(f'#{t + 1} {solution(input_matrix)}')
