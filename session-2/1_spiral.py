
for page in range(10):
    newPage()
    rect(0, 0, width(), height())
    fill(None)
    stroke(1)
    strokeWidth(1)

    with savedState():
        translate(width()/2, height()/2)
        for i in range(200):
            rect(-width()/2, -height()/2, width(), height())
            scale(.98)
            rotate(page)
            
saveImage('spiral.gif')