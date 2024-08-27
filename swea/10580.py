import sys
sys.stdin = open('input.txt', 'r')

# def solution(length, wire_matrixs):
#     """
#     메모리: 52,900 kb
#     실행시간: 274 ms
#     """
#     answer = 0
#     for i, wires in enumerate(wire_matrixs):
#         height = wires[1]
#         for j in range(i + 1, length):
#             if wire_matrixs[j][1] < height:
#                 answer += 1

#     return answer

# TC = int(input())
# for t in range(TC):
#     N = int(input())
#     input_matrix = [list(map(int, input().split())) for _ in range(N)]
#     print(f'#{t+1} {solution(N, sorted(input_matrix))}')



class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)
    
    def update(self, index, value):
        while index <= self.size:
            self.tree[index] += value
            index += index & -index
    
    def query(self, index):
        result = 0
        while index > 0:
            result += self.tree[index]
            print(f'{index & -index} 인덱스')
            index -= index & -index
        return result

def solution(length, wires):
    wires.sort(key=lambda x: x[0])
    max_b = max(b for _, b in wires)
    fenwick_tree = FenwickTree(max_b)
    answer = 0
    
    for _, b in wires:
        answer += fenwick_tree.query(max_b) - fenwick_tree.query(b)
        fenwick_tree.update(b, 1)
    
    return answer

TC = int(input())
for t in range(TC):
    N = int(input())
    wires = [tuple(map(int, input().split())) for _ in range(N)]
    print(f'#{t+1} {solution(N, wires)}')
