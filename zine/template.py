# define our constants
inch = 72
theWidth = 5.83 * inch 
theHeight = 8.27 * inch
bleed = 0.125 * inch

# do i want to see the bleed
# make this false before exporting
drawBleed = True

newPage(theWidth+bleed*2, theHeight+bleed*2)

with savedState():
    if drawBleed:
        stroke(1, 0, 0)
        fill(None)
        strokeWidth(.5)
        rect(bleed, bleed, theWidth, theHeight)
        
# move to the (0, 0) of the cropped page
translate(bleed, bleed)