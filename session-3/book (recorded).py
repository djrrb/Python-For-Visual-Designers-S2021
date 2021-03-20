pageSize = 'Letter'
newPage(pageSize)
stripeCount = 7
# rect() oval() fill()
def triangle(x, y, w, h):
    polygon((0, 0), (w, 0), (w*.25, h))
def marble(x, y, w, h, wiggle=100):
    b = BezierPath()
    b.moveTo((x, y))
    b.lineTo((x+w, y))
    b.lineTo((x+w, y+h))
    b.curveTo((x+w, y+h+randint(-wiggle, wiggle)), (x, y+h+randint(-wiggle, wiggle)), (x, y+h))
    b.closePath()
    drawPath(b)

def background():
    stripeHeight = height()+(height()/stripeCount)
    for stripe in range(stripeCount+1):
        fill(random(), random(), random(), .5)
        marble(0, 0, width(), stripeHeight)
        stripeHeight -= height()/stripeCount

background()

margin = width()/10
marginWidth = width() - margin*2
marginHeight = height() - margin*2
innerWidth = marginWidth - margin*2
innerHeight = marginHeight - margin*2


with open('gatsby-short.txt', 'r', encoding='utf-8') as myFile:
    contents = myFile.read()
    print(contents)
    
    fs = FormattedString(contents, 
        font="MinionPro-Regular",
        fontSize=12,
        lineHeight=18,
        fill=0,
        align="justified",
    )

    while fs:
        newPage(pageSize)
        background()
        translate(margin, margin)
        fill(1)
        rect(0, 0, marginWidth, marginHeight)
        hyphenation(True)
        fs = textBox(fs, (margin, margin, innerWidth, innerHeight))
        
newPage(pageSize)
background()