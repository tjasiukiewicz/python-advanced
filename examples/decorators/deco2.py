


def my_clip(func):
    """ Clip value [0, 100] """

    print("my_deco(...) call")
    def wrapper(*args):
        """ Internal wrapper """
        print("wrapper(...) call")
        result = func(*args)
        if result > 100:
            result = 100
        elif result < 0:
            result = 0
        return result
    wrapper.__doc__ = func.__doc__
    wrapper.__name__ = func.__name__
    return wrapper

@my_clip
def my_add(a, b):
    """ Add two values """
    print("my_add(...) call")
    return a + b


#print(my_add(12, 102))
#print(my_add.__doc__)
print(my_add.__name__)

