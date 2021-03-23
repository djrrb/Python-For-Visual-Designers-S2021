def branch(length, level):
    line((0, 0), (0, length))
    translate(0, length)
    print(level)
    if level < 1:
        return
        
    branchList = [-30*random(), 30*random()]
    for branchAngle in branchList:
        with savedState():
            rotate(branchAngle)
            scale(.8)
            stroke(random(), random(), random())
            branch(length, level-1)


strokeWidth(10)
lineCap('round')
stroke(0)
translate(width()/2, 100)
branch(200, 8)