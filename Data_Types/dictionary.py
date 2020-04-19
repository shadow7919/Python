"""
                                                            Dictionary

unordered collection which have a pair of variable (key : value)
dictionary don't have duplicate they can make by dict()


You can add everyThing to dictionary even another dict by
name ['key'] = value ---> if the key exist it will update value


you can use del or pop to delete item or clear to del all
if you use popitem you get item and del it from dict


You can get all keys by name.keys()
or get all values by name.values()
or both by name.items

You can setdefault('key') to get value of key
if it does't exist it added this key by None value


to add two dictionary use update if it is same key the first one will del
first.update(second)

use dict.fromkeys(listOfKeys , value ) to make a dict with keys
"""

y = dict([('key', 'value')])
print(y)
Dict = {}
print(Dict)

Dict[1] = 'Geeks'
Dict[2] = 'For'
Dict[3] = 1
print(Dict)

Dict['Value_set'] = 2, 3, 4
print(Dict)

Dict[2] = 'Welcome'
print(Dict)
Dict[5] = {'Nested': {'1': 'Life', '2': 'Geeks'}}
print(Dict)
print(Dict[5]['Nested']['2'])
print("Here Where i want to see")

del Dict[5]
Dict.pop(1)
Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}
pop_ele = Dict.popitem()
print(Dict)
print(pop_ele)

Dictionary1 = {'A': 'first'}
Dictionary1.update(B='second', C='third')
print(Dictionary1)
Dictionary2 = {'B': 'change'}
Dictionary1.update(Dictionary2)
print(Dictionary1)

seq = {'a', 'b', 'c', 'd', 'e'}
res_dict = dict.fromkeys(seq)
print(res_dict)
res_dict2 = dict.fromkeys(seq, 1)
print(res_dict2)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
