import sys
sys.stdin = open('input.txt', 'r')


class Direction():
    def __init__(self, dir, n=0):
        self.dir = dir
        self.n = n

    def north(self):
        self.n += 1
        self.dir = self.dir - 90 / 2 ** self.n

    def west(self):
        self.n += 1
        self.dir = self.dir + 90 / 2 ** self.n
        
    def make_fountain(self):
        """
        분수로 만드는 함수
        """
        i = 0
        while True:
            if self.dir - round(self.dir):
                i += 1
                self.dir *= 2
            else:
                break
        return self.dir, i


def solution(string):
    # west
    if len(string) == 4:
        return 90
    # north
    elif len(string) == 5:
        return 0
    # 서북, 북서
    elif len(string) == 9:
        return 45
    else:
        index= len(string) - 1

        # 초기 세팅
        if string[index] == 'h':
            direction = Direction(0)
            index -= 5
        elif string[index] == 't':
            direction = Direction(90)
            index -= 4
        else:
            print('잘못된 입력입니다.')

        # 문자열을 순회하면서 방위 계산
        while 0 < index:
            if string[index] == 'h':
                direction.north()
                index -= 5
            elif string[index] == 't':
                direction.west()
                index -= 4
            else:
                print('과정을 다시 한 번 확인해보세요.')
        
        molecule, denominator = direction.make_fountain()
        return f'{round(molecule)}/{2 ** denominator}'


T = int(input())
for x in range(T):
    input_string = input()
    print(f'#{x+1} {solution(input_string)}')