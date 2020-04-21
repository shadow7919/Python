"""
                                                        Loop technique

enumerate --> give number to iterate
zip --> it is just combine two containers and end if one ends
sorted --> it does't change the containers
set --> for avoid duplicate in use
reversed --> from end to start
"""
fruits = ('banana', 'lemon', 'apple')
for i in enumerate(fruits, 1):
    print(f'{i[0]} : {i[1]}')
print(f"|{20 * '#'}|")
color = ['yellow', 'green', 'red']
for i in zip(fruits, color):
    print(f'{i[0]} is {i[1]}')

numbers = [2, 4, 1, 5, 2, 4, 7, 2, 4, 6]
for i in sorted(numbers):
    print(i, end=' ')
print('compare to -->')
print(*numbers)
for i in set(sorted(numbers)):
    print(i, end=' ')
print('compare to --> ')
print(*numbers)

for i in reversed(range(1, 10, 3)):
    print(i, end=' ')
