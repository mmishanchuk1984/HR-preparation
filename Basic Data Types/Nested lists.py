# https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true#:~:text=Tutorial-,Given%20the%20names%20and%20grades%20for%20each%20student%20in%20a%20class,their%20names%20alphabetically%20and%20print%20each%20name%20on%20a%20new%20line.,-Change%20Theme

students = []
data = []
n = int(input())
for _ in range(n):
    name = input()
    score = float(input())
    students.append(name)
    students.append(score)
    data.append(students)
    students = []

lowest_score_list = []
data.sort(key=lambda x: x[1])
first_lowest_score = data[0][1]
for i in data:
    if first_lowest_score != i[1]:
        students.append(i)
print(students)
second_lowest_score = students[0][1]
for i in students:
    if second_lowest_score == i[1]:
        lowest_score_list.append(i)

lowest_score_list.sort(key=lambda x: x[0])
for i in lowest_score_list:
    print(i[0])



