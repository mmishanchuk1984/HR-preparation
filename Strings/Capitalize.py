# https://www.hackerrank.com/challenges/capitalize/problem?isFullScreen=true


def solve(s):
    data = s.split( )
    result = [i.capitalize() for i in data]
    return  print(' '.join(result))

solve('hello   world  lol')
