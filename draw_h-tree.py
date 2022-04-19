'''
a         c
|         |
|--(x,y)--|
|         |
b         d <
'''

# Time - (c*depth)
# Space - (depth)


def draw_h_tree(x, y, length, depth):
  if depth == 0:
    return
    # draw the 3 line segments of the H-Tree
    # horizontal connecting segment
    drawLine( x -(length // 2) , y, x + (length // 2), y)
    # vertical left segment
    drawLine( x -(length // 2) , y -(length // 2), x -(length // 2) , y + (length // 2))
    # vertical right segment
    drawLine( x + (length // 2) , y -(length // 2), x +(length // 2) , y + (depth // 2))

    a = x -(length // 2) , y + (length // 2)

    b = x -(length // 2) , y - (length // 2)

    c = x +(length // 2) , y + (length // 2)

    d = x +(length // 2) , y - (length // 2)

    # at each stage, the length of segments decreases by a factor of √2
    #draw_h_tree(x -(length // 2), y - (length // 2), length ** (1/2), depth - 1) # lower left  H-tree
    #draw_h_tree(x -(length // 2), y + (length // 2), length ** (1/2), depth - 1) # upper left  H-tree
    draw_h_tree(x +(length // 2), y - (length // 2), length ** (1/2), depth - 1) # lower right H-tree
    draw_h_tree(x +(length // 2), y + (length // 2), length ** (1/2), depth - 1) # upper right H-tree


def drawLine(x1, y1, x2, y2):
  # draws line, assume implementation available
  print("Practice makes Perfect!")
