# def solution(string):
#     alphabet_order = {
#         'a': 1,
#         'b': 2,
#         'c': 3,
#         'd': 4,
#         'e': 5,
#         'f': 6,
#         'g': 7,
#         'h': 8,
#         'i': 9,
#         'j': 10,
#         'k': 11,
#         'l': 12,
#         'm': 13,
#         'n': 14,
#         'o': 15,
#         'p': 16,
#         'q': 17,
#         'r': 18,
#         's': 19,
#         't': 20,
#         'u': 21,
#         'v': 22,
#         'w': 23,
#         'x': 24,
#         'y': 25,
#         'z': 26,
#     }

#     answer = 0
#     for char in string:
#         if alphabet_order.get(char) == answer + 1:
#             answer += 1
#         else:
#             return answer
    
#     return answer

# T = int(input())
# for t in range(T):
#     input_str = input()
#     print(f'#{t+1} {solution(input_str)}')


def solution(string):
    answer = 0
    for char in string:
        if ord(char) - ord('a') == answer:
            answer += 1
        else:
            break
    return answer

T = int(input())
for t in range(T):
    input_str = input()
    print(f'#{t+1} {solution(input_str)}')
