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
    # pseudocode:
    # input is a number equal or greater than 1.
    # output is a list of numbers from 1 to input number
    # create a result list that is empty
    # for item in range of 1  to number
    # append item to the list
    # return list

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')