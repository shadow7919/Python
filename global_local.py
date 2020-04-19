"""
                                                Global and Local Variables


If a variable not define in func It use global
If its define both outSide and Inside it use inside one
If you want to use both in function you should use global key_word
but after you use global the varible value will change
"""


def f():
    print(a)


a = 'out side function'
f()


def g():
    a = 'inside func'
    print(a)


g()
print(a)


def f():
    global a
    print(a)
    a = 'inside f function'


f()
print(a)

a = 1


def f():
    print('Inside f() : ', a)


def g():
    a = 2
    print('Inside g() : ', a)


def h():
    global a
    a = 3
    print('Inside h() : ', a)


print
'global : ', a
f()
print
'global : ', a
g()
print
'global : ', a
h()
print
'global : ', a
