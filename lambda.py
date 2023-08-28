numbers = [1,56,234,87,4,76,24,69,90,135]

def even(a):
    l = []
    for i in a:
        if i % 2 ==0:
            l.append(i)
    return l

is_even = list(map(lambda x:x % 2 == 0, numbers))
print(is_even)