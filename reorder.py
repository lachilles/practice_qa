def reorder(input, n):

    """
    Takes an input array and shifts them in place by n
    Can reverse the array in half at k

    >>> reorder([5,6,7,1,2], 2)
    [2,4,5,6,7,1]

    """
    result = []

    for i, j in enumerate(input):
        (i + n) % len(input)
        return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()