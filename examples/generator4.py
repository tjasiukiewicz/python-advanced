#!/usr/bin/env python3

my_gen = (value for value in ['Ala', 12, 'Zenon'])

print(type(my_gen))
print(dir(my_gen))

for data in my_gen:
    print(data)
