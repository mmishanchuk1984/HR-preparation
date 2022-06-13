# https://www.hackerrank.com/challenges/python-string-split-and-join/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

def split_and_join(line):
    array = line.split()
    joined_line = "-".join(array)
    return joined_line


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
