
#print(6//2)
for y in range(10):
    with savedState():
        for x in range(10):
            if (x % 2 and y % 2) or (not x % 2 and not y % 2):
                fill(1, 0, 0)
            else:
                fill(0, 1, 0)
            oval(0, 0, 100, 100)
            translate(100)
    translate(0, 100)
if 33 % 2:
    print(True)