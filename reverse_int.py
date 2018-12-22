import ipdb

def reverse(x):
    """
    >>> reverse(123)
    321
    >>> reverse(-123)
    -321
    >>> reverse(120)
    21 
    """
    sign = -1 if x < 0 else 1
    solution = 0
    while x != 0:
        x = abs(x)
        pop = x % 10
        solution = (solution * 10) + pop
        x = x // 10
    if not solution.bit_length() < 32:
        return 0
    return solution * sign

if __name__ == '__main__':
    import doctest
    doctest.testmod()