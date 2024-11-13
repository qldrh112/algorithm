import sys
sys.stdin = open('input.txt', 'r')
import copy

def solution(n, m, arr):
   diffs = []
   answer = 0
   left, right = 0, 0

   # 왼쪽, 오른쪽의 보석 개수 찾기
   # 현위치와 보석 위치의 차이 diffs에 요소 추가
   for i in range(n):
      if arr[i] == '1':
         if i < m:
            left +=1
            diffs.append(i - m)
         elif i > m:
            right +=1
            diffs.append(i - m)
         else:
            arr[i] == '0'

   # 한 쪽에 쏠려있다면
   if left == 0 or right == 0:
      return 0


   here = left
   while True:
      copied_diffs = copy.deepcopy(diffs)
      if search_string_1(copied_diffs, here):
         return answer
      else:
         diffs, here, diff = relocate_here(diffs, here)
         answer += diff

def search_string_1(diffs, here):
   while True:
      
      # 한 쪽 끝에 도달해서 인덱스가 터지면 가능한 이동임
      try:
         diffs = list(map(lambda x: x - diffs[here], diffs))
         if abs(diffs[here - 1]) == diffs[here + 1]:
            return False
         # 위치 이동
         elif abs(diffs[here - 1]) > diffs[here + 1]:
            here += 1
         else:
            here -= 1
            
      except IndexError:
         return True

      # 0은 제거함
      diffs = diffs[:here] + diffs[here + 1:]

def relocate_here(diffs, here):
   # 위치 조정
   if abs(diffs[here - 1]) > diffs[here + 1]:
      diff = diffs[here + 1] + diffs[here] // 2 + 1
      diffs = list(map(lambda x: x - diff, diffs))
      return diffs, here + 1, abs(diff)
   
   elif abs(diffs[here - 1] < diffs[here + 1]):
      diff = (diffs[here - 1] + diffs[here]) // 2
      diffs = list(map(lambda x: x - diff, diffs))
      return diffs, here - 1, abs(diff)


T = int(input())
for x in range(T):
   N, M = map(int, input().split())
   input_list = list(input().split())
   # 문제에서 시작점은 0이 아닌 1임
   print(f'#{x + 1} {solution(N, M - 1, input_list)}')