# True, False, None
# use our special none keyword to 
fill(None)
# set the stroke to black
# 0 is the same as 0,0,0
stroke(0)
# set the thickness of the stroke
strokeWidth(10)

# if we want to set line dash, we can use this function
#lineDash(10, 10)

# use a saved state to create a block of code where you can change the state but always go back
with savedState():
    # within our saved state, move to the center of the page
    # use width() and height() to calculate the page dimensions
    translate(width()/2, height()/2)
    # draw a rectangle, subtrating half the width and height so that it draws from the middle rather than drawing from the lower left
    rect(-width()/2, -height()/2, width(), height())
    
    # do a saved state within our other saved state
    with savedState():
        # inside this saved state we will set the fill to red
        fill(1, 0, 0)
        rect(50, 50, 100, 100)
        
    # this circle will no longer be red because it is outside of the savedState() where the fill was set to red
    oval(-50, -50, 100, 100)
    
# now we have outdented again, removing the translate to the center. now this oval will be draw back the bottom left corner
oval(-50, -50, 100, 100)