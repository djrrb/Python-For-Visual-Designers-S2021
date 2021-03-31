# in this demo, we will use random ovals to make a stipple pattern

# move to the center
translate(width()/2, height()/2)

# draw a bunch of dots
for i in range(5000):
    with savedState():
        # enter a saved state
        # calculate X and Y offsets
        # because we are already in the center, we want a random number between a negative and a positive, like (-500, 500)
        offsetX = randint(-width()/2, width()/2)
        offsetY = randint(-height()/2, height()/2)
        # choose a random diameter for our circle
        d = randint(5, 30)
        # move to the offset
        # once we exit the savedState(), we will move back
        translate(offsetX, offsetY)
        # draw the oval, starting half the width and height so that it draws fom the center
        oval(-d/2, -d/2, d, d)

# draw a box in the center, showing that we have exited our saved state
fill(1)
rect(-250, -150, 500, 300)