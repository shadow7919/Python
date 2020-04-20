"""
                                                            Tuple
tuple is almost like list but they are imitable
tuple can have anything inside
You can add two tuple by +
You cant del or add to a tuple after it initialized


enumerate --> make each element a tuple which the first index is iterate number
tuple --> make iterate to tuple
max , min , sum ,sorted

You can use tuple or any iterator on String (Like strip())
"""
name = 'shayan', 'ali', 'this is max'
Tuple1 = (0, 1, 2, 3)
Tuple2 = ('Geeks', 'For', 'Geeks')
Tuple3 = Tuple1 + Tuple2
print(tuple(enumerate(name)))
print(list(enumerate(name, 1)))
print(Tuple3)
print(all(name))
x = tuple('my name')
print(x)