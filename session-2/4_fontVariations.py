# set the font
# either put the font in the same folder as this script, or change the path below
font('CondorVariable-VF.ttf', 200)

# get the variations that exist in the font
print(listFontVariations())

# query the font for its maximum width and weight values
wghtMin = listFontVariations()['wght']['minValue']
wghtMax = listFontVariations()['wght']['maxValue']

# loop through the range of weights
# we have to convert the values from floats to integers, because the range function wants integers
# we will step through the loop by 100, so wght will increase by 100 each time 
for wght in range(int(wghtMin), int(wghtMax), 100):
    # set the font variations
    fontVariations(wdth=70, wght=wght, ital=1)
    # draw the text
    text('Hello world', (0, 0))
    # move the canvas
    translate(0, 100)