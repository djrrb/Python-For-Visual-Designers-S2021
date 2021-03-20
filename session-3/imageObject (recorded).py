im = ImageObject('black-raspberries.jpg')
#im.gaussianBlur()
im.kaleidoscope(6)
imw, imh = im.size()
print(imw, imh)

scaleValue = width()/imw
bottomMargin = ( height() - (imh * scaleValue) ) / 2

translate(0, bottomMargin)

scale(scaleValue)



image(im, (0, 0))