"""
                                                        Switch
You can make a switch case with dictionary
if input wasn't in dictionary by get you can get none
or if we enter second arg it will be replaced
"""

switcher = {
    1: "Doctor",
    2: "Nurse",
    3: "Patient",
}
while True:
    for val in enumerate(switcher.values(), 1):
        print(val[0], '-->', val[1])
    try:
        argument = int(input())
        break
    except ValueError:
        print('input integer')

if switcher.get(argument) is not None:
    print(switcher.get(argument))
else:
    print('Wrong input')
