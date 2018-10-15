def get_cheapest_cost(rootNode):
  # base case check if stack is leaf node
  n = len(rootNode.children)
  if n == 0:
    return rootNode.cost
  else:
    min_cost = 100
    for i in range(0, n - 1):
      temp_cost = get_cheapest_cost(rootNode.child[i])
      if temp_cost < min_cost:
        min_cost = temp_cost
  return min_cost + rootNode.cost



# your code goes here

########################################## 
# Use the helper code below to implement #
# and test your function above           #
##########################################

# A node 
class Node:

  # Constructor to create a new node
  def __init__(self, cost):
    self.cost = cost
    self.children = []
    self.parent = None

    
  def count_cost(self):
    """
    Return a count of how many employees this person manages.
    Return a count of how many people that manager manages. This should
    include *everyone* under them, not just people who directly report to
    them.
    """

    # START SOLUTION
    count = 0
    for child in self.children:
        count = count + self.cost + child.count_cost()

    return count
  
    # O(n)