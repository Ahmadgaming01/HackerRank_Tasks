



def mydecorator(func):
    def inner (*args ):
        print("Start ....")
        func(*args)
        print("End...")

    return inner

@mydecorator
def myprint(x):
    print(x)
myprint ("mahmoud")

@mydecorator

def sum1(y):
    print(y)


sum1 ("sum1")

@mydecorator

def calc1(t):
    print(t)


calc1 ("calc1")


def mydigs(i):
    print(i)


mydigs ("mydigs")



































