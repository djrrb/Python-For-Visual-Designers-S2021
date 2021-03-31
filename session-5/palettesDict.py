# define a colorMap, mapping names to rgb values
colorMap = {
        'fg': (1, 0, 0), # red
        'bg': (0, 1, 0), # green
        'spot1': (0, 0, 1), # blue
        'spot2': (1, 0, 1), # pink
    }

# change this second variable name to color map
# and it will be used instead    
colorMap = {
        'fg': (1, 1, 0), # yellow
        'bg': (.5, 1, .5), # seafoam green
        'spot1': (0, .5, 1), # cyan-ish
        'spot2': (.5, 0, 1), # purple
    }


# draw one rect for each color in the palette
for myColor in colorMap:
    print('\t', myColor, colorMap[myColor])
    fill(*colorMap[myColor])
    rect(0, 0, 300, 300)
    
    with savedState():
        fill(1)
        shadow((1, 1))
        text(myColor, (10, 10))

    translate(150, 150)
    
# call a specific color from our palette and draw an oval
fill(*colorMap['bg'])
oval(0, 0, 300, 300)
