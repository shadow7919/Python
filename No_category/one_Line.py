"""
                                One line condition
in c and java ---> maximum =  a>b ? a : b
in python ---> maximum = a if a>b else b


also you can use tuple or dict or lamda 
I see tuple more useful
True = (x,y)[condition]

"""
a, b, maximum = 4, 9, 0
if a > b:
    maximum = a
else:
    maximum = b
print(maximum)
maximum = a if a > b else b
print(maximum)

a, b = 10, 20
# tuple
print((b, a)[a < b])
# dictionary
print({True: a, False: b}[a < b])
# lamda 
x = (lambda: a, lambda: b)[a < b]
