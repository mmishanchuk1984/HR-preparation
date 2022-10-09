

from itertools import groupby

data = sorted(input())

result = list(groupby(data))
print(result)


