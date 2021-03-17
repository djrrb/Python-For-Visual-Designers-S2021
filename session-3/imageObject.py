# define our image object
im = ImageObject('black-raspberries.jpg')

# apply a filter
# there are SO MANY filters to look through
# https://www.drawbot.com/content/image/imageObject.html
im.gaussianBlur()

# print the size
print(im.size())

# scale it to fit within our canvas
# width of our canvas / width of image
scale(width()/im.size()[0])

# draw the image to the canvas
image(im, (0, 0))