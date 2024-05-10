import heapq


def solution(nums):
    def combination(n, r, k, comb):
        if r == k:
            sum_num = sum([nums[elem] for elem in comb])
            # 중복되는 값은 추가하지 않는다.
            if sum_num not in sums_set:
                sums_set.add(sum_num)
                # 힙의 크기는 5로 유지
                if len(heap) < 5:
                    heapq.heappush(heap, sum_num)
                else:
                    heapq.heappushpop(heap, sum_num)
        else:
            for i in range(comb[k-1] + 1, n):
                comb[k] = i
                combination(n, r, k+1, comb)
    heap = []
    sums_set = set()
    combination(7, 3, 0, [-1] * 3)
    return heap[0]


T = int(input())
for x in range(T):
    input_nums = list(map(int, input().split()))
    print(f'#{x+1} {solution(input_nums)}')