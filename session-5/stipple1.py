translate(width()/2, height()/2)


for i in range(5000):
    with savedState():
        offsetX = randint(-width()/2, width()/2)
        offsetY = randint(-height()/2, height()/2)
        d = randint(5, 30)
        translate(offsetX, offsetY)
        oval(-d/2, -d/2, d, d)
    
fill(1)
rect(-250, -150, 500, 300)