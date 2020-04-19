"""
                                            Packing and Unpacking args

We use  * , ** If our function args are not clear
for tuple or list we use * --> args
for dictionary we use ** --> kwargs

look it first example it is useful
"""

a, b, *c, d = 1, 2, 3, 4, 5, 6, 7, 8, 9
print(a)
print(b)
print(c)
print(d)


def my_sum(*args):
    answer = 0
    for i in args:
        answer += i
    return answer


print(my_sum(1, 2, 3, 4, 5))


def fun(a, b, c):
    print(a, b, c)


d = {'a': 2, 'b': 4, 'c': 10}
fun(**d)


def fun(**kwargs):
    for key in kwargs:
        print(f"{key} = {kwargs[key]}")


fun(name="geeks", ID="101", language="Python")
