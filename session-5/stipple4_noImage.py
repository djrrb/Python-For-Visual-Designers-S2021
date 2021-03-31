# this briefly demos that you can draw things other than images into a clipping path

# make a bezier path and fill it with a formatted string
bp = BezierPath()
fs = FormattedString('A', font='Times', fontSize=1500)
bp.text(fs)

# save our state
# this allows us to exit the clipping path
with savedState():
    # start clipping based on our bezier path
    clipPath(bp)

    # do our stipple stuff
    translate(width()/2, height()/2)
    for i in range(10000):
        with savedState():
            fill(random(), random(), random())
            offsetX = randint(-width()/2, width()/2)
            offsetY = randint(-height()/2, height()/2)
            d = randint(5, 30)
            translate(offsetX, offsetY)
            oval(-d/2, -d/2, d, d)
            
# now we have exited our saved state and clipping path
# draw some text to prove it
font('Verdana', 100)
text('hello world', (200, 200))