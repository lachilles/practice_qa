def move_zeroes(nums):
	"""
	Takes a list of integers and returns same list with zeroes moved to the end

	>>> move_zeroes([0, 1, 0, 3, 12])
	[1, 3, 12, 0, 0]

	"""

	for num in nums:
		if num == 0:
			del num
			nums.append(0)
	return nums

if __name__ == '__main__':
    import doctest
    doctest.testmod()