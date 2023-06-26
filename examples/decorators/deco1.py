

def my_add(a, b):
    print("my_add(...) call")
    return a + b

def clip(func, *args):
    print("clip(...) call")
    result = func(*args)
    if result > 100:
        result = 100
    elif result < 0:
        result = 0
    return result

my_add = clip(my_add, 12, 323)

print(my_add)
