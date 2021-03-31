frames = 60

for frame in range(frames):
    newPage()
    frameDuration(1/15)
    fill(1)
    rect(0, 0, width(), height())
    fill(0)
    translate(width()/frames/2, height()/2)
    for frameDisplay in range(frames):
        if frameDisplay == frame:
            d = 40
        elif frameDisplay == 0:
            d = 0
        else:
            d = 0
        oval(-d/2, -d/2, d, d)
        translate(width()/frames)
        
saveImage('dots.gif')