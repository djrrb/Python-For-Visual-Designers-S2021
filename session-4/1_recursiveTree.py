# based on 

# define a branch function
# it will take a branch length
# and a "level" variable to remember how deep we are in the recursion

def branch(length, level):
    # draw our line between our origin and the length
    line((0, 0), (0, length))
    # move to the tip of the branch before we draw the next branch
    translate(0, length)

    # once our level reaches zero, escape out of the function
    if level < 1:
        return

    # make a list of branches that we will loop through
    # each branch will end by creating two new branches, one at a negative angle and one at a positive angle
    branchList = [-30*random(), 30*random()]
    # loop through the branches
    for branchAngle in branchList:
        # save our state so we return to the tip of the original branch
        with savedState():
            # rotate by our branch angle
            rotate(branchAngle)
            # also make everything smaller
            scale(.8)
            # make our branch a different color, if want
            stroke(random(), random(), random())
            # draw the next branch using the branch function
            # subtract our level by 1 so we are counting down to zero
            # otherwise this goes deeper and deeper and deeper
            branch(length, level-1)



strokeWidth(10)
lineCap('round')
stroke(0)
translate(width()/2, 100)
branch(200, 10)