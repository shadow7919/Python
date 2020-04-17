"""
                                            Main
add def main(): for importing the code not to run
__name__ show if you run or import
it is used if you want to import file someWhere else


                                            faster Input
use stdin.readline is faster and also stdout.write()
it used in special time
"""

from sys import stdin, stdout


def main():
    # array input similar method
    arr = list(map(int, stdin.readline().split()))
    # initialize variable
    summation = 0

    for x in arr:
        summation += x

    # so we need to convert any
    # data into string for input
    stdout.write(str(summation))


# call the main method
if __name__ == "__main__":
    main()