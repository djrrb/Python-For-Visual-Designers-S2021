# define an image object
im = ImageObject('black-raspberries.jpg')
# get its size
w, h = im.size()

# make a new page
newPage(int(w), int(h))

# draw a black background
rect(0, 0, width(), height())

# define the size of our grid
grid = 20
# loop through the height and width of the document
# incrementing by grid
for y in range(0, height(), grid):
    for x in range(0, width(), grid):
        # eyedrop the image at a certain (x, y) value, and set that color to the fill
        fill(*imagePixelColor(im, (x, y)))
        # draw a shape
        oval(x, y, grid, grid)

# now draw the image itself on a new page, for comparison
newPage(int(w), int(h))
image(im, (0, 0))