
'''
a = int(input("Enter first number :"))
b = int(input("Enter secound number :"))
c = []


d = a//b
print(d)
m = a%b
print(m)


c.append(d)
c.append(m)

print(tuple(c))



You are given three integers: , , and . Print two lines.
On the first line, print the result of pow(a,b). On the second line, print the result of pow(a,b,m).



a = int(input("Enter the a"))
b = int(input("Enter the b"))
m = int(input("Enter the m"))


print(pow(a,b))
print(pow(a,b,m))





a,b,m,c,d,r = input("Enter three values: ").split()

print(a,b,m,c,d,r)
'''




a, b, m = (int(input()) for _ in range(3))
print(pow(a,b),pow(a,b,abs(m)),sep="\n")
