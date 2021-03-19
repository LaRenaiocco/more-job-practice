# Given five positive integers, find the minimum and maximum values that 
# can be calculated by summing exactly four of the five integers. Then 
# print the respective minimum and maximum values as a single line of two 
# space-separated long integers.

def min_max(arr):
    """
    >>> min_max([1,2,5,7,9])
    16 24 
    """
    arr.sort()
    total = sum(arr)
    print(total - arr[-1], total - arr[0])

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')