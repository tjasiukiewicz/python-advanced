
def bar():
    print("I'm bar(...)")

def my_deco(func):
    print("my_deco(...) call")
    
    def onuca(func):
        print("I'm onuca(...)")
        return func

    return onuca


@my_deco
def foo():
    pass

foo()

