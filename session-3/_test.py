from colorsys import hsv_to_rgb
from random import choice

def background():
    stripeCount = 10
    wiggle = 150
    stripeHeight = height()/stripeCount
    y = height()+stripeHeight

    with savedState():
        for i in range(stripeCount):
            b = BezierPath()
            b.moveTo((0, 0))
            b.lineTo((width(), 0))
            b.lineTo((width(), y))
            b.curveTo(
                (width(), y+randint(-wiggle, wiggle)),
                (0, y+randint(-wiggle, wiggle)), 
                (0, y)
                )
            b.closePath()
            #blendMode("overlay")
            fill(*hsv_to_rgb(random()/4*2, 1, random()), alpha=1)
            drawPath(b)
            #rect(0, 0, width(), y)
            #polygon((0, y-stripeHeight), (width(), y-stripeHeight), (width()/4, y))
            #drawPath(b)
            y -= stripeHeight



outerMargin = innerMargin = 28

inch = 72
pageWidth = 11/2*inch
pageHeight = 8.5*inch
outerWidth = pageWidth-outerMargin*2
outerHeight = pageHeight-outerMargin*2
innerWidth = outerWidth-innerMargin*2
innerHeight = outerHeight-innerMargin*2
myFontSize = 10

with open('gatsby-short.txt', 'r', encoding="utf-8") as myFile:
    myContents = myFile.read()
    fs = FormattedString(myContents,
        font='Georgia',
        fontSize=myFontSize,
        lineHeight=myFontSize*1.8,
        align="justified",
    )

    for i in range(9):
        newPage(pageWidth, pageHeight)
        background()
        translate(outerMargin, outerMargin)
        fill(1)
        rect(0, 0, outerWidth, outerHeight)
        translate(innerMargin, innerMargin)
        rect(0, 0, innerWidth, innerHeight)
        fill(0)
        hyphenation(True)
        fs = textBox(fs, (0, 0, innerWidth, innerHeight))