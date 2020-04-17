"""
                                                    Input And cast
Python3 use input() to get input from user and output is always a String
We can use Type casting ---> int(input())

                                                    Get more than one input
We use split(splitattr,max_split) to get more than one input
use map and list ---> map out put should cast to something else set,list,...
x = list(map(int,input().split()))
or You can use list comprehension
"""
number = int(input("Input number : "))
x = tuple(map(int, input("Enter a multiple value: ").split()))
print("List of students: ", x)
my_list = [int(x) for x in input().split()]