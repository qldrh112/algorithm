"""
메모리: 62,892 kb
실행시간: 204 ms
"""
from collections import deque


def password_generator():
    # while True 말고 쓸만한 좋은 게 없나?
    while True:
        for i in range(1, 5+1):
            # 음수가 되는 것 검정
            if Deque[0] > i:
                Deque.append(Deque.popleft() - i)
            else:
                Deque.popleft()
                Deque.append(0)
                return Deque


for _ in range(10):
    t = int(input())
    Deque = deque(list(map(int, input().split())))
    print(f'#{t}', *password_generator())