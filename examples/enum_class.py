#!/usr/bin/env python3

from enum import Enum


class MyEnum(Enum):
    SPRING = 0
    WINTER = 1


if __name__ == '__main__':
    e1 = MyEnum.SPRING
    e2 = MyEnum.WINTER
    print(e1 == e2 )
    print(e1 == MyEnum.SPRING )
