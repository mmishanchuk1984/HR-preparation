# https://www.hackerrank.com/challenges/whats-your-name/problem?isFullScreen=true

def print_full_name(first, last):
    data = 'Hello firstname lastname ! You just delved into python'

    data = data.replace('firstname', first)
    data = data.replace('lastname', last)
    return data


print(print_full_name('Nadya', 'Mishanchuk'))
