#!/usr/bin/env python3

my_gen = range(3).__iter__()

print(dir(my_gen))

print(my_gen.__next__())
print(my_gen.__next__())
print(my_gen.__next__())
print(my_gen.__next__())

# 1. Obiekt generatora posiada __iter__()
# 2. Obiekt zwracany z __iter__(), posiada __next__()
# 3. __next__() "odypytywany" jest do momentu rzucenia StopIteration
