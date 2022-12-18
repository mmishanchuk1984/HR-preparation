# https://www.hackerrank.com/challenges/py-collections-namedtuple/problem?isFullScreen=true

from collections import namedtuple

number_of_students = int(input())
column_names = input().split()

id = column_names.index('ID')
name = column_names.index('NAME')
mark = column_names.index('MARKS')
clas = column_names.index('CLASS')

i = 0
student = namedtuple('Student', 'ID MARKS NAME CLASS')
total_marks = 0

while i < number_of_students:
    data = input().split()
    std = student(ID=int(data[id]), MARKS=int(data[mark]), NAME=data[name], CLASS=int(data[clas]))
    total_marks += std.MARKS
    i += 1

average_mark = total_marks / number_of_students
print(f'{average_mark:.2f}')
