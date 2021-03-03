# set our width and height
w, h = 100, 100

for page in range(0, 10):
    newPage()
    fill(1)
    rect(0, 0, width(), height())
    fill(0)
    # get our x and y values by looping through the entire width and height of the canvas, incrementing by 100

    for y in range(0, height(), h):
        for x in range(0, width(), w):
        
            # now here’s the conditional
            # for every shape we draw, flip a coin. if a random value between 0 and 1 is greater than .5, draw an oval. Otherwise, draw a rectangle.
            if random() > .5:
                oval(x, y, w, h)
            else:
                rect(x, y, w, h)

saveImage('~/desktop/conditionals.gif')