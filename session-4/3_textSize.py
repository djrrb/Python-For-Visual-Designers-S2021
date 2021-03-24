# gimme a list of names
names = ["Grimálda Smallburrow", "Merith Yelrora", "Tyrael Travyre", "Baramco Goodwort", "Berthefried von Baggins", "David Lee", "ABCDE"]

# set some constants
margin = 50
marginWidth = width()-margin*2
marginHeight = height()-margin*2

newPage(1000, 1200)

# move in our margin
translate(margin, margin)
for name in names:
        
        # print the name
        font('Georgia')
        # set the font size to 1
        # this means that when we get the text size, it will equal the proportion of width to height
        fontSize(1)
        # get the width and height of this name at 1pt
        w, h = textSize(name)
        # to get our actual font size, divide the margin width by the text width
        # this acts a multiplier that will give us the fontsize that will fill the space
        myFontSize = marginWidth/w
        myLineHeight = myFontSize * 1.2
        # set the font size and draw it
        fontSize(myFontSize)
        text(name, (0, 0))
        # move us up to draw the next line
        translate(0, myLineHeight)