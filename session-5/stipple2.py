# in this demo, we will draw shapes into an image, filter it, and draw it

# define an empty image object
im = ImageObject()

# use the with command to enter the image object
# once inside, we will draw to that image instead of to the canvas
with im:
    # do our stipple stuff inside the image
    # move to center
    translate(width()/2, height()/2)
    # loop through stipples
    for i in range(5000):
        with savedState():
            # set to a random color
            fill(random(), random(), random())
            # get a random x and y offset 
            offsetX = randint(-width()/2, width()/2)
            offsetY = randint(-height()/2, height()/2)
            # get a random diameter
            d = randint(5, 30)
            # move our offset and draw the circle
            translate(offsetX, offsetY)
            oval(-d/2, -d/2, d, d)

# we have existed our image
# so we are now back in the canvas again
# with all of the stuff above existing in im, our ImageObject

# before we draw our image, we can apply filters to it
# here we will make a vortex from the center
im.vortexDistortion((width()/2, height()/2), 500)
# here we will conver the colors to sepia
im.sepiaTone()

# now we can draw the image
image(im, (0, 0))
