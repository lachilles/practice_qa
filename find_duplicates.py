def find_duplicates(arr1, arr2):
  """
  Takes two ordered list of integers of equal length, and returns duplicates found
  O(n+m) time complexity
  O(n), worst case scenario, where n <= m

  >>> find_duplicates([1, 2, 3, 5, 6, 7], [3, 6, 7, 8, 20])
  [3, 6, 7]

  """

  result = []
  i = 0
  j = 0
  
  while i < len(arr1) and j < len(arr2):
    
    if arr1[i] == arr2[j]:
      result.append(arr1[i])
      i += 1
      j += 1
      continue
    
    if arr1[i] < arr2[j]:
      i += 1
      
    else: 
      i += 1
      
  return result


if __name__ == '__main__':
    import doctest
    doctest.testmod()