def int_to_base(num, base):
    """Converts a non-negative integer to an arbitrary base
    Returns an array 
    
    >>> int_to_base(6, 2)
    [1, 1, 0]
    
    """
    if num == 0:
        return []
    quotient = num // base # Integer division
    remainder = num % base
    return int_to_base(quotient, base) + [remainder]


if __name__ == '__main__':
    import doctest
    doctest.testmod()

#This recursive function calculates the digits of a number in a given base from right to left. 
#To see how this works, consider the number 12345. Notice that 12345 % 10 = 5, and 12345 // 10 = 1234. 
#In effect, these two operations allow us to pop the rightmost digit off of a number in base 10.
#We can do these same operations in any other base by changing the 10 in those expressions to an 
#arbitrary integer. Applying these operations recursively gives a wonderfully simple base conversion.