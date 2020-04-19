"""
                                                White space and Line Continuation

use "\" back slash to continue statements
You can use comments by Hash # for single line or Triple Double Quotation marks for more than one line
also in that you can use __doc__ to get comment


                                                ord and chr Ascii cone
to get the ascii code use ord() or to get char with ascii code use chr()
ord('a') ---> 97 , ord ('A') ---> 65 , ord(' ') --> 32
chr(97) ---> a , chr(65) ---> A , chr(10) ---> '\n'


                                                Indentation
Its more important in python some time it is for readability but in
Python it's more and could make syntax problem
which can fix by --->    { Ctrl + Alt + L }  in pycharm

"""
print(__doc__)
x = \
    1 + 2 \
    + 5 + 6 \
    + 10
print(x)
print(ord('a'))
print(chr(97))