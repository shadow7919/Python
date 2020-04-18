"""
                                    String formatting
use , or .format or f String
for number you can use % or : and 0 in both f,d
I normally use f String
it can be used almost every where
"""
name = "shayan"
print("hello my name is ", name.title())
print("hello my name is {}".format(name.title()))
print(f'hello my name is {name.capitalize()}')
a, b, c = 1, 2.56, 3432.314
print("first number is %d , second number is %1.1f" % (a, b))
print("third number is {number3:5.2f}".format(number3=c))
print(f"third number is also {c:09.1f}")
print(f"third number is also {c:9.1f}")
peron = {'name': 'shayan', 'age': 19}
print(f"Name : {peron['name']} , age : {peron['age']}")