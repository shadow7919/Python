"""
                                                        String
You can make a String with '' , "" , or triple "
when you use one you should't use same in String
and for multiple line String use triple cote


Strings are immutable you can't change a single char or del it
but you can del a hole String


and you can access a char of String by string[n]
or part of String by String[n : n+7]
n can be either + nor - if you use - it's count from end
You can reverse a string by [::-1]

formatting String with f string is best way
You can use f"{string:}" and with : you can use formatting
you can use --->  left = < , right = > , middle = ^ with a number show how many char

"""
string = "hello"
print(string)
print(string[::-1])  # Reverse
print(string[:3])
print(string[-5:2])
# more than one line String
String1 = '''Geeks 
For
Life'''
print(String1)
# Use format for its place
print(f"middle ---> |{'Hello':^20}|")
print(f"left ---> |{'Hello':<20}|")
print(f"right ---> |{'Hello':>20}|")

String1 = f"{'company':<16} was founded in {2009:<4}!"
print(String1)