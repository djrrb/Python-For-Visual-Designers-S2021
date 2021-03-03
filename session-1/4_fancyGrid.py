
x = 0
y = 0
print(random())
for yiteration in range(0, 10):
    for xiteration in range(0, 10):
        print(xiteration)
        fill(random(), random(), random())
        #cmykFill(1, 0, 0, .5)
        rect(x, y, 100, 100)
        x += 100
        # x = x + 100
    y += 100
    x = 0