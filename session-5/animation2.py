def lerp(start, stop, amt):
	return float(amt-start) / float(stop-start)
def norm(value, start, stop):
	return start + (stop-start) * value
def remap(value, start1, stop1, start2, stop2, withinBounds=False):
    factor = lerp(start1, stop1, value)
    if withinBounds:
        if factor < 0: factor = 0
        if factor > 1: factor = 1
    return norm(factor, start2, stop2)


frames = 60

fontPath = 'Condor Variable'
font(fontPath)
variations = listFontVariations()
for variation in variations:
    print(variations[variation])
    for infoItem in variations[variation]:
        print(infoItem)


wghtMin = variations['wght']['minValue']
wghtMax = variations['wght']['maxValue']

italMin = variations['ital']['minValue']
italMax = variations['ital']['maxValue']

wdthMin = variations['wdth']['minValue']
wdthMax = variations['wdth']['maxValue']


for frame in range(frames):
    newPage()
    frameDuration(1/15)
    fill(1)
    rect(0, 0, width(), height())
    fill(0)
    with savedState():
        translate(width()/frames/2, height()/2)
    
        x = 0
    
        for frameDisplay in range(frames):
            if frameDisplay == frame:
                d = 40
            elif frameDisplay == 0:
                d = 10
            else:
                d = 20
            y = sin(2*pi * frameDisplay/frames) * height()/2
            oval(x-d/2, y-d/2, d, d)
            x += width()/frames
    
    yprogress = sin(2*pi * frame/frames)
    wghtValue = remap(yprogress, -1, 1, wghtMin, wghtMax)

    wdthProgress = cos(2*pi * frame/frames)
    wdthValue = remap(wdthProgress, -1, 1, wdthMin, wdthMax)
    
    italValue = remap(frame, 0, frames, italMin, italMax)

    fs = FormattedString('hi', font=fontPath, fontSize=600, align="center", fontVariations={'wght': wghtValue, 'wdth': wdthValue, 'ital': italValue}
    )
    
    textBox(fs, (0, 0, width(), height()-200))
        
saveImage('dots.gif')