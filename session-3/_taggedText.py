# generate indesign tagged text
# is there a newer XML style? idk

# this is what we start the tagged text with
taggedTextPrefix = """<ASCII-MAC>
<Version:15.1><FeatureSet:InDesign-Roman><ColorTable:=<Black:COLOR:RGB:Process:1,1,1>>
<DefineParaStyle:NormalParagraphStyle=<Nextstyle:NormalParagraphStyle>>
<ParaStyle:NormalParagraphStyle>"""

# we will start with our prefix and add to this string
taggedText = taggedTextPrefix

# define some constants
fontName = 'Minion Pro'
romanName = ''
italicName = 'Italic'
theSize = 12
theLineHeight = theSize*1.5
m = 50
paragraphCount = 0

# open the text file we are going to parse
with open('gatsby-short.txt', 'r', encoding="utf-8") as myFile:
    # read the contents
    contents = myFile.read()
    # split the contents into paragraphs
    paragraphs = contents.split('\n')
    
    # make a formatted string for drawbot
    fs = FormattedString(
        font=fontName,
        fontSize=theSize,
        lineHeight=theLineHeight,
        )
        
    # loop through the paragraphs
    for paragraph in paragraphs:

        # set the particular font for this paragraph
        # if paragraph is odd, use italic
        # tagged text wants the family and style name separate
        # drawbot wants them together, so we gotta keep track of both
        fullName = fontName
        styleName = romanName
        if paragraphCount % 2:
            styleName = italicName
            fullName = fontName + ' ' + italicName
        # add a tab to all but the first paragraph
        indent = ''
        if paragraphCount != 0:
            indent = '\t'
            
        # choose the paragraph color randomly, like we do
        r, g, b = random(), random(), random()
        
        # i couldn’t get tagged text working with unicode, so for this example I’m converting curly quotes to straight quotes. You can choose “Use Typographer’s Quotes” to convert them back
        # https://practicaltypography.com/straight-and-curly-quotes.html
        simplifiedParagraph = paragraph.replace('“', '"').replace("‘", "'").replace("”", '"').replace("’", "'")
        
        # okay, now use an f string to write the tagged text, and append it to our big taggedText variable. This allows us to put our variables right in the string.
        taggedText += f"<cColor:COLOR:RGB:Process: {r},{g},{b}><cFont:{fontName}><cTypeface:{styleName}>{simplifiedParagraph}<cTypeface:><cFont:>\n"
        
        # also append the paragraph to our formatted string for drawbot
        fs.append(indent+paragraph+'\n', fill=(r, g, b), font=fullName)
    
        # keep track of our paragraph count
        paragraphCount += 1
            
            
    # write a tagged text file, using "w" write-mode
    with open('taggedText.txt', 'w', encoding="utf-8") as ttFile:
        ttFile.write(taggedText)
        
    # draw our formatted string
    while fs:
        newPage('Letter')
        fs = textBox(fs, (m, m, width()-m*2, height()-m*2))
        