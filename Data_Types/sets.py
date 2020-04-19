"""
                                                        set

Set is an unordered collection, mutable, has no duplicate element
Set normally is use to compare


add
you can add one element to set by add
for more than one you can use update
You can add tuple but you can't add list like single element
tuple is hashable ; but list is not


delete set's element
you can use discard or remove but if element
does't exist remove raise error and discard don't
with clear you can del all elements


you can print a set in for but because its not ordered
you can't get a element of set


compare tow set
union --> return a set without duplicate and all element from sets --> A U B
intersection( --> return a same element in both sets --> A ⋂ B
difference --> return a set which del elements in first if they are in second --> A - B
symmetric_difference --> return a set which have the element not in both --> (A - B) U (B - A )

"""
x = {1, 2, 3, 4, 5, 2, 4, 2, 6}
x.remove(2)
x.discard(1)
x.update(('reza', 'hamid'))
x.add('shayan')
y = x.copy()
y.remove(3)
print(x)
print(y)
first = {1, 2, 3, 4, 5}
second = {3, 4, 5, 6, 7}
print(first.union(second))
print(first.intersection(second))
print(first.difference(second))
print(first.symmetric_difference(second))
