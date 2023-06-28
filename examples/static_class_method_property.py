#!/usr/bin/env python3

class X:
    attr1 = 12
    attr2 = 45

    def __init__(self):
        self.__arg1 = 12
        self.__arg2 = "ala"

    @staticmethod
    def get_attr1():
        return X.attr1

    @classmethod
    def show_class_name(cls):
        return cls.__name__

    @property
    def arg1(self):
        return self.__arg1

    @arg1.setter
    def arg1(self, value):
        self.__arg1 = value

    @arg1.deleter
    def arg1(self):
        del self.__arg1

    def _get_arg2(self):
        return self.__arg2

    def _set_arg2(self, value):
        self.__arg2 = value

    arg2 = property(
            fget = _get_arg2,
            fset = _set_arg2,
            fdel = None,
            doc = "Access to attr2"
    ) 


if __name__ == '__main__':
    x = X()
    print(X.attr1)
    print(x.attr1)
    print(x.get_attr1())
    print(x.show_class_name())
    print(X.show_class_name())
    print(x.arg1)
    x.arg1 = 123
    x.arg2 = 333
