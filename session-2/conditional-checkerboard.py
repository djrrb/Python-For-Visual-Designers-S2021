# conditional checkerboard

# set a value to use for the width and height of our grid items
baseGrid = 20
# how many times does our grid fit into our document? Figure that out and add one for good measure. We could also just use a big number here...
xiterations = width()//baseGrid+1
yiterations = height()//baseGrid+1

# loop through our rows
for yi in range(yiterations):
    # save our state
    # this will allow us to reset the x value to 0 by exiting the saved state
    with savedState():
        # loop through our columns
        for xi in range(xiterations):
            # to make a checkerboard, we want to draw a shape only if:        
            # - both the x and y columns are odd
            # - both the x and y columns are even

            # in any given 2x2 matrix, we want this:
            #     0   1
            #    --------
            # 1 |   | X |
            # 0 | X |   |
            
            # first, let’s do odd x + odd y 
            # (the upper right of a 2x2 matrix)
            # this is functionally the same as writing
            # if yi % 2 == 1 and yi % 2 == 1:
            if yi % 2 and xi % 2:
                # draw a red square
                fill(1, 0, 0)
                rect(0, 0, baseGrid, baseGrid)
                
            # now let’s do even x + even y
            # (the lower left of a 2x2 matrix)
            if xi % 2 == 0 and yi % 2 == 0:
                # draw a black circle
                fill(0, 0, 0)
                oval(0, 0, baseGrid, baseGrid)
                
            # if neither of the above conditions are met,
            # we draw nothing and the loop just continues
            
            # move to the right so we’re ready to draw the next column
            translate(baseGrid, 0)
            
    # outdenting exits our saved state and x is returned to 0
    # now move our y up for the next row
    translate(0, baseGrid)

saveImage('~/desktop/conditional-checkerboard.png')