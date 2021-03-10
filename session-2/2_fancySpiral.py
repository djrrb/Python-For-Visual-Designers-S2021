# import the hsv_to_rgb converter
from colorsys import hsv_to_rgb

# define starting values for hue, saturation, and value
h = 0
s = 1
v = 1

# loop through our pages
for page in range(360):
    # make a new page with a black background
    newPage()
    rect(0, 0, width(), height())
    
    # start a saved state
    # right now this isn’t useful because we don’t draw anything after we center the document, but it doesn’t hurt
    with savedState():
        # move us to the center of the document
        translate(width()/2, height()/2)
        #skew(30)
        
        # draw a buncha squares
        for i in range(200):
            # if our iteration is odd, get a color
            # of our iteration is even, use black
            # this uses the modulo operator, which gives us the remainder of division
            # 5 // 2 = 2 (2 goes into 5 two times)
            # 5 % 2 = 1 (2 goes into 5 two times, with a REMAINDER of 1)
            
            # https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences 
            if i % 2:
                fill(*hsv_to_rgb(h, s, v))
                h += .02
            else:
                fill(0, 0, 0)
            # draw a rectangle
            # subtract the starting point by half the width and height, effectively drawing it from the center 
            rect(-width()/2, -height()/2, width(), height())
            # after each rectangle, scale the canvas so it will draw smaller next time
            scale(.98)
            # rotate the canvas by the number of degrees that happens to be equal to our page number (360 pages = full rotation)
            rotate(page)
            
# outdent all the way to save the final image one time
saveImage('spiral.gif', antiAliasing=True)