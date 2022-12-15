# https://www.hackerrank.com/challenges/word-order/problem?isFullScreen=true

from collections import Counter

number_of_words = int(input())
cnt = 0
lst = []

while cnt < number_of_words:
    word = input()
    lst.append(word)
    cnt +=1

distinct_words = len(set(lst))
print(distinct_words)
occurrences = Counter(lst)
for key, value in occurrences.items():
    print(value, end=' ')








