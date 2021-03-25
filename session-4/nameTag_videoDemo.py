import csv

def background(grid=30, invert=False):
    im = ImageObject('black-raspberries.jpg')
    if invert:
        im.colorInvert()
        im.colorControls(saturation=1, brightness=-.9, contrast=1.5)
    else:
        im.colorControls(saturation=None, brightness=-.3, contrast=None)

    offsetX = randint(0, 250)
    offsetY = randint(0, 250)

    rect(0, 0, width(), height())
    for y in range(0, height(), grid):
        for x in range(0, width(), grid):
            fill(*imagePixelColor(im, (x+offsetX, y+offsetY)))
            oval(x, y, grid, grid)
           
with open('Fantasy Conference  - Sheet1.csv', encoding="utf-8") as myFile:
    rows = csv.reader(myFile)
    for i, row in enumerate(rows):
        if i == 0:
            continue
        name, affiliation, role = row
 
        newPage(500, 300)
        if role.lower() == 'speaker':
            background(16, invert=True)
        else:
            background(16)
            
        margin = width()/15
        marginWidth = width()-margin*2
        marginHeight = height()-margin*2
        myFontSize = 100
        

        
        with savedState():
            font('FormaDJRBanner-Bold', myFontSize)
            lineHeight(myFontSize*.9)
            
            
            results = FormattedString(font='FormaDJRBanner-Bold', fontSize=myFontSize, lineHeight=myFontSize*.9, fill=1)
            for word in name.split(' '):
                tw, th = textSize(word)
                if tw < marginWidth:
                    results.append(word+' ')
                else:
                    results.append(word+' ', fontSize=myFontSize*marginWidth/tw, lineHeight=myFontSize*marginWidth/tw*.8)
            
            fill(1)
            shadow((5, -5), blur=5, color=None)
            textBox(results, (margin, margin, marginWidth, marginHeight))
            
            
        if affiliation:
            font('FormaDJRText-Regular')
            fontSize(13)
            lineHeight(13)
            fill(.1)
            rect(0, margin-5, width(), 21)
            fill(1)
            textBox(affiliation, (margin, margin, marginWidth, 13))
        if i > 10:
            break
