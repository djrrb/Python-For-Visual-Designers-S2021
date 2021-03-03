scale(.5)

x = 0
y = 0
for i in range(10):
    image('myGrid.pdf', (x, y), pageNumber=i)
    x += 171