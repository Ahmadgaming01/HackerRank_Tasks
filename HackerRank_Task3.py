from collections import namedtuple
'''
5
ID         MARKS      NAME       CLASS     
1          97         Raymond    7         
2          50         Steven     4         
3          91         Adrian     9         
4          72         Stewart    5         
5          80         Peter      6
'''

N = int(input('Enter the number of students : '))
headers = input('Enter the list elements :')
student = namedtuple('Student',headers)
students = []
for i in range(N):
    students.append(student(*input('Enter the name of student and marks :').split()))
print( sum(map(lambda x: float(x.MARKS),students))/len(students))
