import csv

def background():
    rect(0, 0, width(), height())
    im = ImageObject('black-raspberries.jpg')
    grid = 20
    offsetx = randint(0, 500)
    offsety = randint(0, 500)
    for y in range(0, height(), grid):
        for x in range(0, width(), grid):
            #print(imagePixelColor(im, (x, y)))
            fill(*imagePixelColor(im, (x+offsetx, y+offsety)))
            oval(x, y, grid, grid)
    #image(im, (0, 0))



with open('Fantasy Conference  - Sheet1.csv', encoding="utf-8") as myFile:
    rows = csv.reader(myFile)
    
    for rowNumber, row in enumerate(rows):
        if rowNumber == 0:
            continue
        name, affiliation, role = row
        print(name)
        newPage(500, 300)
        background()
        font('Helvetica', 1)
        words = name.split(' ')
        for word in words:
            w, h = textSize(word)
            print(word, w)
            fontSize(width()/w)
            fs = FormattedString(font='Helvetica', fontSize=width()/w)
            for char in word:
                myFontSize = width()/w+randint(-10, 10)
                fs.append(char, fill=1, stroke=(random(), random(), random()), strokeWidth=myFontSize/50, fontSize=myFontSize)
            textBox(fs, (0, 0, width(), height()))
        if rowNumber > 4:
            break
        
    
        