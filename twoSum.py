import doctest

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]

    >>>twoSum([2, 7, 11, 15], 9)
    [0, 1]

    >>>twoSum([2, 3, 4, 5], 9)
    [2, 3]

    >>>twoSum([2, 3, 4, 5], 6)
    [0, 2]
    """

    for i, num in enumerate(nums):
        r = []
        while len(r) != 2 and target > 0:
            target -= num
            r += i


if __name__ == '__main__':
    doctest.testmod() 
