# run a loop for every page
for page in range(0, 10):
    # make a new page
    newPage(1000, 1000)
    
    # draw a black background the size of the canvas
    rect(0, 0, 1000, 1000)
        
    # define x and y variables that we can change as we go
    x = 0
    y = 0

    # loop through all the rows
    for yiteration in range(0, 10):
        # loop through all the columns
        for xiteration in range(0, 10):
            print(xiteration)
            
            # set the fill to a random color
            fill(random(), random(), random())
            rect(x, y, 100, 100)

            # instead of drawing an oval, load an image
            # we will use savedState() to save our place in the code
            # we didn’t cover this yet, but the savedState() funtion allows us to scale the image to 10% inside the indent and move to the grid position inside the indent, and then go back to where we were outside the indent
            with savedState():
                translate(x, y)
                scale(1/10)
                image('myGrid.pdf', (0, 0))
            x += 100
            # x = x + 100
        y += 100
        x = 0
        
saveImage('~/desktop/metagrid.gif')