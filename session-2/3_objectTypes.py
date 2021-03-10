from random import choice

# define a string that we will mess with
myString = 'Hello World it’s me'
print('STRING STUFF')
print('='*20)
# more string methods at
# https://docs.python.org/3/library/string.html

# use len() to get the number of items in a list
print('length:', len(myString))
print('first character:', myString[0])
print('last character:', myString[-1])
print('slice:', myString[0:5])
print('loop through string:')
for char in myString:
    print('\t', char) # the '\t' adds a tab

print('Uppercase', myString.upper())
print('Lowercase', myString.lower())

# get a random word, either using a slice or using the choice function
print('Get random letter:', myString[randint(0, len(myString)-1)])
print('Get random letter:', choice(myString))


# split the string into a list, using space as a delimiter
myWords = myString.split(' ')

print('\n\nLIST STUFF')
print('='*20)
# https://docs.python.org/3/tutorial/datastructures.html

# lists are written with square brackets
print(myWords)
# use len() to get the number of items in a list
print('word length', len(myWords))
# use square brackets to get a slice
print('first word', myWords[0])
print('last word', myWords[-1])

print('loop:')
for word in myWords:
    print('\t', word)
# get a random word, either using a slice or using the choice function
print('Get random word:', myWords[randint(0, len(myWords)-1)])
print('Get random word:', choice(myWords))

# a tuple is like a package of other objects
# https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences
print('\n\nTUPLE STUFF')
print('='*20)

# define a tuple, like x, y coordinates
coords = (100, 200)
print(coords)
# use square brackets to get a slice
print('x value', coords[0])
print('y value', coords[1])
print('loop through tuple:')
for value in coords:
    print('\t', value)