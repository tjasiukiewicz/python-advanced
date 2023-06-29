#!/usr/bin/env python3

#print("I'm my_module")
#print(__name__)

AUTHOR="Tom"
VERSION="1.0.1"

__all__ = ['foo']

def foo():
    print('foo() function')

def bar():
    print('bar() function')

#print("In my_module")


if __name__ == '__main__':
    print("In main")
