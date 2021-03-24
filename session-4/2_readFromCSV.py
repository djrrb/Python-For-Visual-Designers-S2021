# import the library we will use to parse the csv
import csv

# open our file with the proper encoding
with open('Fantasy Conference  - Sheet1.csv', encoding="utf-8") as myFile:
    # read the csv
    rows = csv.reader(myFile)
    # if we use the enumerate() function, we can define the row and its index at the same time
    # this helps us keep track of where we are
    for i, row in enumerate(rows):
        # skip the first row, because it is the header
        if i == 0:
            continue
        # unpack our row into three columns
        name, affiliation, role = row
        # print the name
        print(name)
