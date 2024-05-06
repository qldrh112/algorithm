"""
메모리: 45,196 kb
실행시간: 100 ms
"""
def days_to_sunday():
    return next_sunday.get(S)


next_sunday = {
    'SUN': 7,
    'MON': 6,
    'TUE': 5,
    'WED': 4,
    'THU': 3,
    'FRI': 2,
    'SAT': 1,
}
T = int(input())
for t in range(T):
    S = input()
    print(f'#{t+1} {days_to_sunday()}')