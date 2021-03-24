import csv

inch = 72

def background(grid=10):
    im = ImageObject('black-raspberries.jpg')   
    im.colorControls(saturation=None, brightness=-.5, contrast=None) 
    xoffset = randint(0, 500)
    yoffset = randint(0, 500)
    rect(0, 0, width(), height())
    for y in range(0, int(height()), grid):
        for x in range(0, int(width()), grid):
            fill(*imagePixelColor(im, (x+xoffset, y+yoffset)))  
            oval(x, y, grid, grid)

def badge(name, affiliation=None, role=None):
    background()
    names = name.split(' ')
    m = width()/20
    mw = width()-m*2
    mh = height()-m*2
    with savedState():
        fill(1)
        fontSize(45)
        lineHeight(40)
        font('FormaDJRBanner-Bold')
        shadow((-3, -3), 5, (0, 0, 0))
        textBox(name, (m, m, mw, mh))

    fill(0)
    fontSize(10)
    lineHeight(10)
    rect(m, m, width(), 16)
    font('FormaDJRText-Regular')
    fill(1)
    textBox(affiliation, (m+5, m+1.5, mw, 12))

with open('/Users/david/Documents/Education/CooperType/Python-For-Visual-Designers-S2021/session-4/Fantasy Conference  - Sheet1.csv', encoding="utf-8") as csvfile:
    rows = csv.reader(csvfile)
    for i, row in enumerate(rows):
        if i == 0:
            continue
        newPage(8.5/2*inch, 11/4*inch)
        print(row, row[0])
        badge(
            name=row[0],
            affiliation=row[1],
            role=row[2]
        )
        if i > 0:
            pass
        