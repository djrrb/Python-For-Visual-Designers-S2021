docSize = 'Letter'
newPage(docSize)
stripeCount = 7

# this is a triangle function
# we are not using it but we could
def triangle(x, y, w, h):
    polygon((0, 0), (w, 0), (w*.25, h))

# this is a marble function
# it takes our standard x, y, width, height arguments like a rect()
# and also an option wiggle attribute
def marble(x, y, w, h, wiggle=100):
    # define a Bezier Path object
    b = BezierPath()
    # move to our x, y starting position
    b.moveTo((x, y))
    # draw a line across the bottom of the shape
    b.lineTo((x+w, y))
    # draw a line up the righthand side
    b.lineTo((x+w, y+h))
    # draw a curve across the top
    # this is a series of three points
    # - handle #1
    # - handle #2
    # the next oncurve point (the upper left of our shape)
    # for both handles, allow their y value to vary by a random amount
    b.curveTo(
        (x+w, y+h+randint(-wiggle, wiggle)), 
        (x, y+h+randint(-wiggle, wiggle)), 
        (x, y+h)
    )
    # close our path to complete the shape
    b.closePath()
    # draw it to the canvas
    drawPath(b)
   
def background(): 
    # This function draws our background
    # a series of marble stripes
    # we start drawing a shape that is the full height of the page
    # and then make the stripeHeight progressively smaller
    stripeHeight = height()
    # loop through each stripe
    for stripe in range(stripeCount):
        # set our fill to a random color and make it semitransparent
        fill(random(), random(), random(), .5)
        # run the marble function, passing it x,y,w,h
        # we can also optionally pass it a wiggle argument
        # otherwise it just uses the default built into the function
        marble(0, 0, width(), stripeHeight, wiggle=200)
        # every time, reduce our stripe height
        stripeHeight -= height()/stripeCount

# define some constants
myFontSize = 14
# define line height relative to font size
myLineHeight = myFontSize*1.5

myFont = 'MinionPro-Regular'
bookTitle = 'The Great Gatsby'
pageNumber = 1

# draw the background on our first empty page
background()

# open our text file
with open('gatsby-short.txt', 'r', encoding="utf-8") as myFile:
    # read the contents into a string that we’re calling contents
    contents = myFile.read()
    # load the contents into a formatted string
    # also attach whatever attributes we want to
    fs = FormattedString(contents, 
            font=myFont, 
            fontSize=myFontSize, 
            lineHeight=myLineHeight, 
            #openTypeFeatures=dict(smcp=True), 
            align="justified", 
            firstLineIndent=myLineHeight
        )
    
    # make new pages until we run out of text in the formatted string
    while fs:
        newPage(docSize)
        # define some variables related to margins and margin size
        m = width()/10
        # define our top margin separately to make room for a header
        topMargin = m*1.5
        outerWidth = width()-m*2
        outerHeight = height()-m*2
        innerWidth = outerWidth-m*2
        # for this one, incorporate our top margin value
        innerHeight = outerHeight-m-topMargin
        
        # draw the background for each page
        background()
        # move in to our outer margin
        translate(m, m)
        # draw a white background that we will put text over
        fill(1)
        rect(0, 0, outerWidth, outerHeight)
        # turn on hyphenation
        hyphenation(True)
        # draw a text box with the formatted string
        # the text box will return the overflow to us
        # so we will catch it by reassigning fs
        # this way, we whittle down fs until there is no text left
        fs = textBox(fs, (m, m, innerWidth, innerHeight))
        
        # we didn’t do this during class, but why not draw some running heads
        header = FormattedString(bookTitle, 
            font=myFont, 
            fontSize=myFontSize, 
            lineHeight=myLineHeight, 
            openTypeFeatures=dict(smcp=True), 
        )
        # and a page number, aligned to the right
        # use the onum (oldstyle figures) opentype feature
        formattedPageNumber = FormattedString(str(pageNumber), 
            font=myFont, 
            fontSize=myFontSize, 
            lineHeight=myLineHeight, 
            openTypeFeatures=dict(onum=True), 
            align="right", 
            
        )
        # draw these up top, adding the topMargin to the innerHeight
        text(header, (m, topMargin+innerHeight))
        text(formattedPageNumber, (m+innerWidth, topMargin+innerHeight))
    
        pageNumber += 1
        
newPage(docSize)
background()