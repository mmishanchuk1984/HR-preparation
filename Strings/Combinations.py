# https://www.hackerrank.com/challenges/itertools-combinations/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

from itertools import combinations

data = input().split()
text = sorted(data[0])
k = int(data[1])

for i in range(1, k+1):
    perm_list = list(combinations(text, i))
    for el in perm_list:
        print(''.join(el))
