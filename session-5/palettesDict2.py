import random

palettes = {
    
    'primary': {
        'fg': (1, 0, 0),
        'bg': (0, 1, 0),
        'spot1': (0, 0, 1),
        'spot2': (1, 0, 1),
    },
    
    'other': {
        'fg': (1, 1, 0),
        'bg': (.5, 1, 0),
        'spot1': (0, .5, 1),
        'spot2': (0, 0, 1),
    }

    
    
    }


# get the keys from the dict using the keys method, convert that to a list, and then use random.choice() to choose a color palette
colorMapName = random.choice(list(palettes.keys()))

print('use palette', colorMapName)

# define colorMap variable by pulling a palette from our palettes dict
colorMap = palettes[colorMapName]

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
fill(*colorMap['spot1'])
oval(0, 0, 300, 300)
