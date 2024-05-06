import sys
sys.stdin = open('C:/Users/didie/Documents/gs_repo/algorithm/python/input.txt', 'r')

"""
65 - 0
90 - 25
대문자면 65빼고
소문자면 71빼고
숫자면 아스키에서 4 더하고
+: 43 -> 62
/: 47 -> 63
"""

"""
1. 문자열을 base64 규칙에 따라 변환(2진수로)
2. 8bit씩 잘라서 아스키 값으로 변환
"""

def decoding_base64(string):
    """
    string: base64로 encoding 된 문자열
    return: base64로 decoding 한 2진수(str)
    """
    output = ''
    for char in string:
        # char이 숫자면
        if str.isdigit(char):
            output += '0' * (6 - len(bin(ord(char) + 4)[2:])) + bin(ord(char) + 4)[2:]
        # char이 '+' 면
        elif char == '+':
            output += bin(62)[2:]
        # char이 '/' 면
        elif char == '/':
            output += bin(63)[2:]
        # char이 대문자면
        elif str.isupper(char):
            output += '0' * (6 - len(bin(ord(char) - 65)[2:])) + bin(ord(char) - 65)[2:]
        # char이 소문자면
        else:
            output += '0' * (6 - len(bin(ord(char) - 71)[2:])) + bin(ord(char) - 71)[2:]
    return output


def bin_to_ascii(string):
    """
    string: 8의 배수의 bit로 이루어진 2진수 덩어리
    return: 아스키코드로 변형한 문자열
    """
    output = ''
    for i in range(len(string)//8):
        output += chr(int(string[8 * i : 8 * (i + 1)], 2))
    return output


T = int(input())
for t in range(T):
    input_str = input()
    print(f'#{t+1} {bin_to_ascii(decoding_base64(input_str))}')