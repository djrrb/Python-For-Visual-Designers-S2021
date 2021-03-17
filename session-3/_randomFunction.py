
def printAThing(thing='default'):
    print(thing)
    rect(randint(0, 200), randint(0, 200), 100, 100)
    fontSize(200)
    text(thing, (randint(0, 1000), randint(0, 1000)))


for name in ['Barley', 'Ashokan', 'Wing', 'Electricity', 'Plant']:
    oval(0, 0, 20, 20)
    printAThing(name)
