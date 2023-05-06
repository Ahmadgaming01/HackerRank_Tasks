'''
5
ID         MARKS      NAME       CLASS     
1          97         Raymond    7         
2          50         Steven     4         
3          91         Adrian     9         
4          72         Stewart    5         
5          80         Peter      6
'''
'''
from collections import namedtuple
Point = namedtuple('Point','x,y')


from collections import namedtuple


student = namedtuple('student','ID, marks, name, Class')


std1 = student(ID = 1, marks = 97, name = 'Raymond', Class = '7')
std2 = student(ID = 2, marks = 50, name = 'Steven', Class = '4')
std3 = student(ID = 3, marks = 91, name = 'Adrian ', Class = '9')
std4 = student(ID = 4, marks = 72, name = 'Stewart', Class = '5')
std5 = student(ID = 5, marks = 80, name = 'Peter', Class = '6')
total = float(std1.marks+std2.marks+std3.marks+std4.marks+std5.marks)

print (total/5)


Car(Price=100000, Mileage=30, Colour='Cyan', Class='Y')
print (xyz.Class)




students = [student._make(list(input().strip().split())) for _ in range(n)]
print(sum([int(student.MARKS) for student in students]) / len(students))


from collections import namedtuple
n = int(input('1'))

student = namedtuple("column", (list(input('2').strip().split())))


students = [student._make(list(input('3').strip().split())) for x in range(n)]
#print(sum([int(student.MARKS) for student in students]) / len(students))

print(students)



from collections import namedtuple
N = float(input('1'));student = namedtuple('student',input('2').strip().split())
print(sum(float(student(*input('3').strip().split()).MARKS) for _ in range(N))/N)
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
N = int(input('Enter the number of students : '))
headers = input('Enter the list elements :')
student = namedtuple('Student',headers)
students = []
for i in range(N):
    students.append(student(*input('Enter the name of student and marks :').split()))
print( sum(map(lambda x: float(x.MARKS),students))/len(students))


