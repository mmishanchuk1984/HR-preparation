# https://www.hackerrank.com/challenges/python-mutations/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

def mutate_string(string, position, character):
    first_part = string[:position]
    second_part = string[position + 1:]
    result = first_part + character + second_part
    print(result)


mutate_string('abracadabra', 5, 'k')
