def even(x):
    return x % 2 == 0

list1 = [1,2,3,4,5,6,7,8,9,0]
print(list(filter(even, list1)))