import doctest

def is_prime(n):
    """Skills assessed: math, for loop

    >>> is_prime(7)
    True
    >>> is_prime(15)
    False
    >>> is_prime(143)
    False
    >>>

    """

    # Get the sqrt of n, and remove decimals by converting to int
    m = int(n ** (.5))
    # Trial division up to m + 1 to accomodate 3
    for i in range(2, m + 1):
        # Fail fast
        if (n % i) == 0:
            return False
    return True


if __name__ == '__main__':
    doctest.testmod()
