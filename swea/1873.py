# import sys
# sys.stdin = open('input.txt', 'r')

# # 문자열은 못 바꿈
# class Tank:
#     def __init__(self, maps, tank_y, tank_x):
#         self.maps = maps
#         self.tank_y = tank_y
#         self.tank_x = tank_x

#     def up(self):
#         maps[self.tank_y][self.tank_x] = '^'
#         if self.tank_y > 0 and maps[self.tank_y - 1][self.tank_x] == '.':
#             maps[self.tank_y][self.tank_x], maps[self.tank_y - 1][self.tank_x] = '.', '^'
#             self.tank_y -= 1

#     def down(self):
#         maps[self.tank_y][self.tank_x] = 'v'
#         if self.tank_y < H and maps[self.tank_y + 1][self.tank_x] == '.':
#             maps[self.tank_y][self.tank_x], maps[self.tank_y + 1][self.tank_x] = '.', 'v'
#             self.tank_y += 1

#     def left(self):
#         maps[self.tank_y][self.tank_x] = '<'
#         if self.tank_y > 0 and maps[self.tank_y][self.tank_x - 1] == '.':
#             maps[self.tank_y][self.tank_x], maps[self.tank_y][self.tank_x - 1] = '.', '<'
#             self.tank_x -= 1

#     def right(self):
#         maps[self.tank_y][self.tank_x] = '<'
#         if self.tank_y < W and maps[self.tank_y][self.tank_x + 1] == '.':
#             maps[self.tank_y][self.tank_x], maps[self.tank_y][self.tank_x + 1] = '.', '>'
#             self.tank_x += 1

#     def shoot(self):
#         i = 0
#         if maps[self.tank_y][self.tank_x] == '^':
#             while self.tank_y + i > 0:
#                 i -= 1
#                 if maps[self.tank_y + i][self.tank_x] == '*':
#                     maps[self.tank_y + i][self.tank_x] = '.'
#                 elif maps[self.tank_y + i][self.tank_x] == '#':
#                     return

#         elif maps[self.tank_y][self.tank_x] == 'v':
#             while self.tank_y + i < H - 1:
#                 i += 1
#                 if maps[self.tank_y + i][self.tank_x] == '*':
#                     maps[self.tank_y + i][self.tank_x] = '.'
#                 elif maps[self.tank_y + i][self.tank_x] == '#':
#                     return

#         elif maps[self.tank_y][self.tank_x] == '<':
#             while self.tank_x + i > 0:
#                 i -= 1
#                 if maps[self.tank_y][self.tank_x + i] == '*':
#                     maps[self.tank_y][self.tank_x + i] = '.'
#                 elif maps[self.tank_y][self.tank_x + i] == '#':
#                     return

#         else:
#             while self.tank_x + i < W - 1:
#                 i += 1
#                 if maps[self.tank_y][self.tank_x + i] == '*':
#                     maps[self.tank_y][self.tank_x + i] = '.'
#                 elif maps[self.tank_y][self.tank_x + i] == '#':
#                     return


# def tank_location(height, width):
#     tanks = ['^', '<', '>', 'v']
#     for h in range(height):
#         for w in range(width):
#             if maps[h][w] in tanks:
#                 return (h, w)
    

# def solution(H, W, maps, commands):
#     tank_y, tank_x = tank_location(H, W)
#     tank = Tank(maps, tank_y, tank_x)
#     for command in commands:
#         if command == 'U':
#             tank.up()
#         elif command == 'D':
#             tank.down()
#         elif command == 'L':
#             tank.left()
#         elif command == 'R':
#             tank.right()
#         else:
#             tank.shoot()
#     return maps


# T = int(input())
# for t in range(T):
#     H, W = map(int, input().split())
#     maps = [list(input()) for _ in range(H)]
#     N = int(input())
#     commands = input()
#     maps = solution(H, W, maps, commands)
#     print(f'#{t+1}', end=' ')
#     for i in range(H):
#         for j in range(W):
#             if j == W - 1:
#                 print(maps[i][j])
#             else:
#                 print(maps[i][j], end=' ')

import sys
sys.stdin = open('input.txt', 'r')

class Tank:
    def __init__(self, maps, tank_y, tank_x):
        self.maps = maps
        self.tank_y = tank_y
        self.tank_x = tank_x
        self.directions = {
            'U': ('^', -1, 0),
            'D': ('v', 1, 0),
            'L': ('<', 0, -1),
            'R': ('>', 0, 1)
        }

    def move(self, direction):
        dir_char, dy, dx = self.directions[direction]
        ny, nx = self.tank_y + dy, self.tank_x + dx
        self.maps[self.tank_y][self.tank_x] = dir_char
        if 0 <= ny < len(self.maps) and 0 <= nx < len(self.maps[0]) and self.maps[ny][nx] == '.':
            self.maps[self.tank_y][self.tank_x], self.maps[ny][nx] = '.', dir_char
            self.tank_y, self.tank_x = ny, nx

    def shoot(self):
        dir_char = self.maps[self.tank_y][self.tank_x]
        dy, dx = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}[dir_char]
        ny, nx = self.tank_y, self.tank_x
        while True:
            ny, nx = ny + dy, nx + dx
            if not (0 <= ny < len(self.maps) and 0 <= nx < len(self.maps[0])):
                break
            if self.maps[ny][nx] == '*':
                self.maps[ny][nx] = '.'
                break
            elif self.maps[ny][nx] == '#':
                break

def tank_location(maps):
    tanks = {'^', '<', '>', 'v'}
    for y, row in enumerate(maps):
        for x, cell in enumerate(row):
            if cell in tanks:
                return y, x
    return -1, -1

def solution(H, W, maps, commands):
    """
    실행시간: 54,520 kb
    메모리: 242 ms
    """
    tank_y, tank_x = tank_location(maps)
    tank = Tank(maps, tank_y, tank_x)
    for command in commands:
        if command in 'UDLR':
            tank.move(command)
        elif command == 'S':
            tank.shoot()
    return maps

T = int(input())
for t in range(T):
    H, W = map(int, input().split())
    maps = [list(input()) for _ in range(H)]
    N = int(input())
    commands = input()
    result_maps = solution(H, W, maps, commands)
    print(f'#{t+1}', end=' ')
    for row in result_maps:
        print(''.join(row))