# The median of a list of numbers is essentially its middle element after s
# orting. The same number of elements occur after it as before. Given a list 
# of numbers with an odd number of elements, find the median?

def find_median(arr):
    """
    >>> find_median([5, 3, 1, 2, 4])
    3
    """
    arr.sort()
    median = len(arr) // 2
    return arr[median]

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')