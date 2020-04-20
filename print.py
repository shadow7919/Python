"""
                                            Print
end
in python3 default after print it has new line
with ,end = ' '  you can change it '\t','\b'

sep
this will show how you want to separate the args to print

print a list with out bracket
You can do it with *name , sep
or you can use " ".join()
"""
print("hello man ", end='\t')
print("this is it ", end='\n')
print(1, 2, 3, 4, 5, sep='\t', end='\t finished\n')

name = 'shayan', 'ali', 'morteza'
numbers = [1, 2, 3, 4, 5]
print(*name, sep=', ')  # or
print(', '.join(name))
# you cant use .join for integer 
print(*numbers, sep=' and ')
