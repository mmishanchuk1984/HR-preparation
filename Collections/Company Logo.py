# https://www.hackerrank.com/challenges/most-commons/problem?isFullScreen=true

from collections import Counter

s = input()

occurrences = Counter(s)

sorted_dict = dict(sorted(occurrences.items(), key=lambda x: (-x[1], x[0])))
counter = 0

for key, value in sorted_dict.items():
    counter +=1
    print(f'{key} {value}')
    if counter == 3:
        break


