
fontName = 'Verdana'
fv = {'wght': 700, 'wdth': 100}
def drawBadge(name, dimensions, speaker=None,  affiliation=None, ):
    margin =dimensions[0]/10
    newPage(*dimensions)
    words = name.split(' ')
    words.reverse()
    marginWidth = dimensions[0]-margin*2
    marginHeight = dimensions[1]-margin*2
    
    blockHeight = 0
    wordsToDraw = []
    for word in words:
        fs = FormattedString(word, fontSize=1, lineHeight=1, font=fontName)
        w, h = textSize(fs)
        myFontSize = marginWidth/w
        myLineHeight = myFontSize * .8
        angle = randint(-5, 5)
        wordsToDraw.append((word, myFontSize, myLineHeight, angle))
        blockHeight += myLineHeight
        
    translate(margin, margin)
    
    bottomBump = (marginHeight-blockHeight)/2
    if affiliation:
        fontSize(8)
        lineHeight(10)
        font(fontName)
        textBox(affiliation, (0, 0, marginWidth, 12), align="center")
        bottomBump += 10
        
    print(blockHeight, marginHeight)
    if blockHeight > marginHeight :
        scale(marginHeight/blockHeight)
    translate(marginWidth/2, 0)
    translate(0, bottomBump)
    with savedState():
        for word, myFontSize, myLineHeight, angle in wordsToDraw:
            with savedState():
                rotate(angle, (marginWidth/2, myLineHeight/2))
                fill(None)
                #fill(random(), random(), random(), .5)
                stroke(0)
                strokeWidth(.2)
                rect(-marginWidth/2, 0, marginWidth, myFontSize)
            translate(0, myLineHeight)
 
    for word, myFontSize, myLineHeight, angle in wordsToDraw:
        with savedState():
            rotate(angle, (marginWidth/2, myLineHeight/2))
            font(fontName, myFontSize)
            fs = FormattedString(font=fontName, fontSize=myFontSize, lineHeight=myFontSize, stroke=0, fill=None, strokeWidth=myFontSize/50)
            for letter in word:
                fs.append(letter, stroke=(random(), random(), random()))
            text(fs, (-marginWidth/2, -fontDescender()))
        translate(0, myLineHeight)
    
    
drawBadge('David Jonathan Ross', (400, 300), affiliation='Stuff & Co.', )
drawBadge('Thequickbrown foxjumpsover', (100, 100), affiliation='Stuff & Co.')