# define formatted string
fs = FormattedString('', font='Georgia', fontSize=12)
for fontName in installedFonts():
    if fontName[0] != '.':
        fs.append(fontName, font=fontName, fill=(random(), random(), random()) )

pages = 5
while fs:
    newPage()
    fs = textBox(fs, (0, 0, width(), height()))
