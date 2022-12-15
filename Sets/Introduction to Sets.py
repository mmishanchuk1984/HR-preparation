# https://www.hackerrank.com/challenges/py-introduction-to-sets/problem?isFullScreen=true

def average(array):
    data = set(array)
    result = sum(data)/len(data)
    return result

print(average([15, 45, 32]))
