# https://www.hackerrank.com/challenges/python-string-formatting/problem?isFullScreen=true
number = 17
for i in range(1, number + 1):
    print(f'{i} {str(oct(i)[2:])} {str(hex(i)[2:].capitalize())} {str(bin(i)[2:])}')
