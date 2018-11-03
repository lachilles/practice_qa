def all_unique(lst):
    """
    Takes a list and returns boolean if all items are unique
    
    >>> all_unique(['apple', 'berry', 'cherry', 'durian'])
    True
    >>> all_unique(['apple', 'berry', 'cherry', 'apple'])
    False

    """

    return len(set(lst)) == len(lst)

# implement without creating a dict

if __name__ == '__main__':
    import doctest
    doctest.testmod()