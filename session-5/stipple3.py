# in this demo, we will draw shapes into an image, and render that image within a clipping path

# define an empty bezier path
bp = BezierPath()

# define a formatted string
fs = FormattedString('A', font='Times', fontSize=1500)

# draw our formatted string into the bezier path
# this is like “create outlines” in illustrator
# converting text into shapes
bp.text(fs)

# make an empty image object
im = ImageObject()

# draw our texture into the image
with im:
    # move to center
    translate(width()/2, height()/2)
    # make a lot of dots
    for i in range(10000):
        with savedState():
            # random color
            fill(random(), random(), random())
            # random position
            offsetX = randint(-width()/2, width()/2)
            offsetY = randint(-height()/2, height()/2)
            # random diameter
            d = randint(5, 30)
            # move and draw
            translate(offsetX, offsetY)
            oval(-d/2, -d/2, d, d)

# now we are back in the main canvas
# pass our already-defined BezierPath to the clipPath() function
# anything after this will be drawn inside our bp
clipPath(bp)

# apply our image filters
im.vortexDistortion((width()/2, height()/2), 500)
im.sepiaTone()
# draw an image
image(im, (0, 0))
