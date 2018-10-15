import doctest

def pangram(string):
    """ function that checks if each letter of the alphabet is used in the input at least once.
    
    >>> pangram("the quick brown fox jumps over the lazy dog")
    True
    >>> pangram("abc")
    False
    
    """
    used = {char.lower() for char in string if char.isalpha()}
    return len(used) == 26


if __name__ == '__main__':
    doctest.testmod()