# https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=true

def swap_case(s):
    s = list(s)
    result = ''
    for i in s:
        if i.islower():
            i = i.upper()
            result += i
        else:
            i = i.lower()
            result += i
    return result


print(swap_case('aaaaBBB'))
