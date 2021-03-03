# in this script we’re gonna make a multipage colorful grid

# run a loop for every page
for page in range(0, 10):
    # make a new page
    # all code at this indent level will run 10 times
    newPage(1000, 1000)
    
    # the default background is transparent. if we want, we can draw a black background the size of the canvas.
    rect(0, 0, 1000, 1000)
    
    # if this is an animation, we can set a frame duration in seconds
    frameDuration(1)
    
    # define x and y variables that we can change as we go
    x = 0
    y = 0

    # loop through all the rows
    for yiteration in range(0, 10):
        # loop through all the columns
        # all code at this indent level will run 10x10=100 times
        for xiteration in range(0, 10):
            # everything at this indent level will run 10x10x10=1000 times
             
            # set the fill to a random color
            # fill(red, green, blue)
            # values between 0 and 1
            fill(random(), random(), random())
            # CYMK also possible
            #cmykFill(1, 0, 0, .5)
            
            # draw a shape
            # oval(x, y, w, h) or rect(x, y, w, h)
            oval(x, y, 100, 100)
            # after we draw the shape, move to the right
            x += 100
            # this is the same as
            # x = x + 100
            
        # ok, we are out of the inner loop now
        # bump up the y 
        y += 100
        # reset the x so that our column starts at 0
        x = 0
        
# go back to no indent, this code will only run once
# save the image
# the extension of the filename determines the format
saveImage('myGrid.gif')
