"""
                                                    Compare variable or object

if you want to compare value use == but
if you want to compare reference use is


for check something is in iterator use in
if you want to check variable type or to check obj of class
isinstance(x,type) , isinstance(obj,class)
"""
x = 2
y = 2
c = 1
print(x is y)
print(c is y)

my_list = x, y, c
print(c in my_list)
print(x in my_list)

print(isinstance(x, int))


class Car:
    def __init__(self):
        pass


car = Car()
print(isinstance(car, Car))
