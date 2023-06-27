#!/usr/bin/env python3

class A:
    def __init__(self):
        print('Class A __init__() method')

    def method(self):
        print('Class A method() method')

class B(A):
    def __init__(self):
        print('Class B __init__() method')
        print('*')
        print('    call parent')
        #A.__init__(self)
        super().__init__()

    def method(self):
        print('Class B method() method')
        print('*')
        print('    call parent')
        #A.method(self)
        super().method()

class C(A):
    def __init__(self):
        print('Class C __init__() method')
        print('*')
        print('    call parent')
        #A.__init__(self)
        super().__init__()

    def method(self):
        print('Class C method() method')
        print('*')
        print('    call parent')
        #A.method(self)
        super().method()

class D(C,B):
    def __init__(self):
        print('Class D __init__() method')
        print('*')
        print('    call parent')
        #B.__init__(self)
        #C.__init__(self)
        super().__init__()

    def method(self):
        print('Class D method() method')
        print('*')
        print('    call parent')
        #B.method(self)
        #C.method(self)
        super().method()


if __name__ == '__main__':
    d = D()
    print('-' * 20)
    d.method()

    print(D.__mro__)

