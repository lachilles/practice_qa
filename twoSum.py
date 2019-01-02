import doctest

def twoSum(nums, target):
    """
    Given a list of integers, return indices of the two numbers such that they add up to a specific target.
    
    >>> twoSum([2, 7, 11, 15], 9)
    [0, 1]

    >>> twoSum([2, 3, 4, 5], 9)
    [2, 3]

    >>> twoSum([2, 3, 4, 5], 6)
    [0, 2]
    """

    seen = {
        # 2: 0,
        # 3: 1,
        # 4: 2,
        # 5: 3
    }
    for i, num in enumerate(nums):
        if target - num in seen:
            return [seen[target - num], i]
        seen[num] = i


if __name__ == '__main__':
    doctest.testmod() 
