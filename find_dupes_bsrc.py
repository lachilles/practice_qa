from math import floor

def find_duplicates_bsrc(lst1, lst2):
  """
  Takes two ordered list of integers of unequal length, and returns duplicates found
  We are running a binary search on lst2 N times.
  O(N⋅log(M)) time complexity
  Space complexity is O(n), worst case scenario, where n <= m

  >>> find_duplicates_bsrc([1, 2, 3, 4, 5, 7], [3, 4, 6, 7, 8, 20])
  [3, 4, 7]

  """
  result = []

  for number in lst1:
    if binary_search(lst2, number) != -1:
      result.append(number)

  return result


def binary_search(lst, num):
  start = 0
  end = len(lst) - 1

  while start <= end:
    # get the midpoint
    mid = start + floor((end - start) // 2 )
    # if num is greater than num in middle of lst, increment start pointer by 1 from mid
    if lst[mid] < num:
      start = mid + 1
    # if num in middle of list is the num I'm looking for, return
    elif lst[mid] == num:
      return mid
    # decrement end pointer by 1 from mid
    else:
      end = mid - 1

  return -1

if __name__ == '__main__':
    import doctest
    doctest.testmod()