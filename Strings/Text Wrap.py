# https://www.hackerrank.com/challenges/text-wrap/problem?isFullScreen=true

import textwrap


def wrap(string, max_width):
    res = textwrap.fill(string, max_width)
    return res


wrap('ABCDEFGHIJKLIMNOQRSTUVWXYZ', 4)

