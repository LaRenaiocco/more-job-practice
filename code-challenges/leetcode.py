#Reverse Integer - easy
# Given a signed 32-bit integer x, return x with its digits reversed. If reversing
#  x causes the value to go outside the signed 32-bit integer 
#  range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers 
# (signed or unsigned).

def reverse_integer(num):
    """
    >>> reverse_integer(123)
    321
    >>> reverse_integer(-123)
    -321
    >>> reverse_integer(120)
    21
    >>> reverse_integer(0)
    0
    """
    result = ""
    if num < 0:
        negative = True
    elif num > 0:
        negative = False
    else:
        return num

    str_num = str(num)
    if negative:
        str_num = str_num[1:]
    str_num = list(str_num)
    
    while len(str_num) > 0:
        last = str_num.pop()
        result += last
    
    if negative and int(result) * -1 >= -2 ** 31 :
        return int(result) * -1
    elif int(result) < (2 ** 31) -1:
        return int(result)
    else: 
        return 0

# pseudocode:
# check if number is negative
# if so store as a boolean variable
# convert integer to a string
# if negative, slice off first char (the - character)
# while len string is greater than 0
# pop off last character
# append to new string for reversed number
# convert new string back to int
# if negatative boolean is true
# return new int * -1
# else return new int

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print('\n ALL TESTS PASSED!\n')