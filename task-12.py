n = 5
clac1 = n*2-1
for x in range(n):
    char = "H"*(x*2+1)
    print(char.center(clac1," "))


for i  in range (n):
    mit = "H"*n
    print(mit.center(clac1) + mit.rjust(clac1))
