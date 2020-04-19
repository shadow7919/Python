"""
                                                        list

lists are mutable and good for iterate it can add or del
lists can hold anything
you can get items in list like String []


adding to list
You can add a anything with append to list
if you want a position to add use insert
if you want to add all elements of something use extend


remove
remove an element by value ---> remove
or by index ---> pop , by default it del the last index
you can del all element by clear


extra
get index of item by index()
get count of items in list
reserve a list by list.reserve or [::-1]
sort --> sort the list
get a copy of list ---> if you don't want to change org list


print a list with out bracket
You can do it with *name , sep
or you can use " ".join()
"""

name = ('asghar', 'reza','amirhossein')
list = [1, 2, 3, 4, 5]
list.insert(1, "shayan")
print(list)
list.extend([1, 2, 3, 4, 5, 6])
list.pop(0)
list.remove(3)
print(list.count(1))
print(list.index(3))
print(list)
print(list[1:4])
cop = list.copy()
cop.clear()
print(list)
numbers = [1,2,3,4,5]
print(*name,sep=', ') # or
print(', '.join(name))
# for number you just have first
print(*numbers,sep=' and ')