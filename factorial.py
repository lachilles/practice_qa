def factorial(num):
    """
    Takes an int and returns the factorial recursively

    >>> factorial(6)
    720
    >>> factorial(1)
    1
    >>> factorial(3)
    6

    """

    if num == 1:
        return num
    else:
        return num * factorial(num - 1)


if __name__ == '__main__':
    import doctest
    doctest.testmod()