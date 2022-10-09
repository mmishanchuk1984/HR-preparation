# https://www.hackerrank.com/challenges/itertools-permutations/problem?isFullScreen=true

from itertools import permutations

data = input().split()
text = data[0]
k = int(data[1])


perm_list = sorted(list(permutations(text, k)))
for i in perm_list:
    print(''.join(i))









