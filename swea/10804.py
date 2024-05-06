def solution(string):
    mirror_char_maps = {
        'b': 'd',
        'd': 'b',
        'p': 'q',
        'q': 'p',
    }
    answer = [mirror_char_maps[x] for x in string][::-1]

    return ''.join(answer)


T = int(input())
for t in range(T):
    input_string = input()
    print(f'#{t+1} {solution(input_string)}')