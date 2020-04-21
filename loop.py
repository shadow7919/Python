"""
                                                            Loop
While and For

keyword that been used with this are
range --> for iterate in numbers
else --> after it finished
break --> get out of loop
continue --> pass from one condition
pass --> empty loop
"""
count = 0
while count < 3:
    count = count + 1
    print("Hello")
else:
    print("Else Block")

my_list = ["geeks", "for", "geeks"]
for index in range(len(my_list)):
    print(my_list[index])
for i in my_list:
    print(i)

for letter in 'shayan':
    if letter == 'y' or letter == 's':
        continue
    print('Current Letter :', letter)

for letter in 'geeksforgeeks':
    pass
