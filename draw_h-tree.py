
'''
a         c
|         |
|--(x,y)--|
|         |
b         d <


Time - (c*depth)
Space - (depth)
'''
def draw_h_tree(x, y, length, depth):
  if depth == 0:
    return
    # horizontal
    drawLine( x -(length // 2) , y, x + (length // 2), y)
    # vertical left
    drawLine( x -(length // 2) , y -(depth // 2), x -(length // 2) , y + (length // 2))
    # vertical right
    drawLine( x + (length // 2) , y -(depth // 2), x +(length // 2) , y + (depth // 2))

    a = x -(length // 2) , y + (length // 2)
    a = (x -.. )

    b = x -(length // 2) , y - (depth // 2)

    c = x +(length // 2) , y + (length // 2)

    d = x +(length // 2) , y - (depth // 2)


    draw_h_tree(x -(length // 2), y - (length // 2), length ** (1/2), depth - 1)
    draw_h_tree(x -(length // 2), y + (length // 2), length ** (1/2), depth - 1)
    draw_h_tree(x +(length // 2), y - (length // 2), length ** (1/2), depth - 1)
    draw_h_tree(x +(length // 2), y + (length // 2), length ** (1/2), depth - 1)
    
drawLine(x1, y1, x2, y2):
  
print "Practice makes Perfect!"   
