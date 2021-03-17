# conditional checkerboard

# loop through rows
for y in range(10):
    # save our state for each row
    # so we can go back after drawing the columns
    with savedState():
        # loop through the columns
        for x in range(10):
            # here’s our big conditional
            # if x is odd AND y is odd OR x is even AND y is even:
            if (x % 2 and y % 2) or (not x % 2 and not y % 2):
                # make it red
                fill(1, 0, 0)
            else:
                # otherwise, make it green
                fill(0, 1, 0)
            # draw our oval
            oval(0, 0, 100, 100)
            # move to the right
            translate(100)
    # go back to our saved state
    # move it up
    translate(0, 100)