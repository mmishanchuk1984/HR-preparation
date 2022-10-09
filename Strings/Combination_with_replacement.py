# https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

from itertools import combinations_with_replacement

data = (input().split())
text = sorted(data[0])
k = int(data[1])


perm_list = list(combinations_with_replacement(text, k))
for el in perm_list:
    print(''.join(el))
