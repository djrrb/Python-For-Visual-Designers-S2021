frames = 60

# make a new page for each frame
for frame in range(frames):
    newPage()
    # set the frame duration to 15 FPS
    frameDuration(1/15)
    
    # make a background
    fill(1)
    rect(0, 0, width(), height())
    fill(0)
    
    # move to half the height so we can see our dots
    translate(width()/frames/2, height()/2)
    
    # now loop through frames AGAIN
    # we will draw a representation of each frame as a dot
    for frameDisplay in range(frames):
        
        # determine dot size using if/elif/else
        if frameDisplay == frame:
            # for our current frame, make the dot big
            d = 40
        elif frameDisplay == 0:
            # for the first frame, make the dot tiny
            d = 5
        else:
            # for all other frames, make the dot small
            d = 10
            
        # draw the dot, centered on our origin
        oval(-d/2, -d/2, d, d)
        # move to the next column
        translate(width()/frames)
        
# save our gif
saveImage('dots.gif')