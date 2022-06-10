# https://www.hackerrank.com/challenges/python-tuples/problem?isFullScreen=true#:~:text=Tutorial-,Task%0AGiven%20an%20integer%2C,.,-Sample%20Input%200

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t = tuple(integer_list)
    hash_num = str(hash(t))
    print(hash_num)


print('Hello')
