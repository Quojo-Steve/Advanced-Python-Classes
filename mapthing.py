list1 = [1,2,3]

def square(x):
    return x * x

def sqr(x):
    return x**2

print(list(map(sqr,map(square,list1))))





