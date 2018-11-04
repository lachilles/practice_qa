def find_duplicates_python(arr1, arr2):
 """
  Takes two list of any length, and returns duplicates found
  O(n+m) time complexity
  O(n), worst case scenario, where n <= m

  >>> find_duplicates_python([1, 2, 3, 4, 5, 7], [3, 4, 6, 7, 8, 20])
  [3, 4, 7]

  """
  return set(arr1) & set(arr2)


if __name__ == '__main__':
    import doctest
    doctest.testmod()