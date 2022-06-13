# https://www.hackerrank.com/challenges/find-a-string/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

def count_substring(string, sub_string):
    counter = 0
    step = len(sub_string)
    for i in range(len(string)):

        text = string[i:step]
        if text == sub_string:
            counter += 1
        step += 1

    print(counter)


count_substring('ABCDCDC', 'CDC')
