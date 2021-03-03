x = 0
y = 0

for yiteration in range(0, 10):
    for xiteration in range(0, 10):
        print(xiteration)
        rect(x, y, 100, 100)
        x += 100
        # x = x + 100
    y += 100
    x = 0