#!/usr/bin/env python3

class A:
    def __init__(self):
        pass

    def __del__(self):
        pass

    def method(self):
        print('Class A method()')

    def _method(self):
        print('Class A _method()')

    def __method(self):
        print('Class A __method()')

    def show(self, name):
        print('Class A show() method name=%s' % name)


class B(A):
    def __init__(self):
        pass

    def __del__(self):
        pass

    def method(self):
        print('Class B, call method A.method()')
        A.method(self)


if __name__ == '__main__':
    a = A()
    b = B()

    b.method()
    b._method()
    b._A__method() # W praktyce, jakieś wyjątkowe zastosowania !??

    B.show(b, 'on class B')
    b.show('on object type B')
