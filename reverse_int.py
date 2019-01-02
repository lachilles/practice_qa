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
        x = abs(x)  # Convert to absolute for easy parsing
        pop = x % 10  # get first digit in x
        solution = (solution * 10) + pop  # increase unit of current solution and add popped off digit
        x = x // 10  # bind new value to x after popping off first digit
    if not solution.bit_length() < 32:
        return 0
    return solution * sign

if __name__ == '__main__':
    import doctest
    doctest.testmod()