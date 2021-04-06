# 8kyu - Pre Fizz workout
# This is the first step to understanding FizzBuzz.

# Your inputs: a positive integer, n, greater than or equal to one. n is provided, 
# you have NO CONTROL over its value.

# Your expected output is an array of positive integers from 1 to n (inclusive).

# Your job is to write an algorithm that gets you from the input to the output.
def pre_fizz(n):
    """
    >>> pre_fizz(1) 
    [1]
    >>> pre_fizz(2)
    [1, 2]
    >>> pre_fizz(3)
    [1, 2, 3]
    >>> pre_fizz(4)
    [1, 2, 3, 4]
    >>> pre_fizz(5)
    [1, 2, 3, 4, 5]
    """
    result = []
    for num in range(1, n + 1):
        result.append(num)

    return result

#  MORE CONCISE SOLUTION

    # return list(range(1, n+1))

    # pseudocode:
    # input is a number equal or greater than 1.
    # output is a list of numbers from 1 to input number
    # create a result list that is empty
    # for item in range of 1  to number
    # append item to the list
    # return list

# 8 kyu - price of mangoes
# There's a "3 for 2" (or "2+1" if you like) offer on mangoes. For a given quantity 
# and price (per mango), calculate the total cost of the mangoes.

def mango(quantity, price):
    """ 
    >>> mango(3, 3)
    6
    >>> mango(9, 5)
    30
    """ 

# pseudocode:
# input quantity of mangoes and price per mango
# output is a dollar amount for the number of mangoes purchased
# We can figure out the number of mangoes that will be bought/number free
# by using floor division on quanity divided by 3
# the result will be the number of free mangoes
# subtract result from total quanity to get number that must be purchased
# multiply number purchased by price per mango for return value


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')