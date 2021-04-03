pages = 20
for page in range(pages):
    newPage()
    frameDuration(1/5)
    # set a margin
    m = 50

    # make an empty list
    colorList = []

    # populate that list by adding random colors to it!
    for i in range(10):
        # define my color
        myColor = random(), random(), random()
        # add my color to the list
        colorList.append(myColor)


    # set a gradient as the fill color
    # gradient takes the following arguments:
    # - the start point of the gradient
    # - the end point of the gradient
    # - a list of colors
    # - optionally, a list of positions between zero and one (this allows you to have each band of color be different widths)

    linearGradient(
        (0, 0), # start point
        (width(), height()), # end point
        colorList, # list of colors
        )
    
    # draw a background
    rect(0, 0, width(), height())

    # draw the same gradient but going the other direction
    linearGradient(
        (width(), 0), # start point
        (0, height()), # end point
        colorList, # list of colors
        )
    shadow((20, -20), 100)
    # draw an oval using our gradient
    oval(m, m, width()-m*2, height()-m*2)

saveImage('~/desktop/gradients.mp4')