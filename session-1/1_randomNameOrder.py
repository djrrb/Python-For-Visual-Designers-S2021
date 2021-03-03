# define names as a string
nameString = """Tarragon Mangobug
Apogee Daywhite
Lightning Daisyshine
Albedo Quickcone
Winnie Cedarblossom
Pine Woodblossom
Oregano Pearfoam
Lark Broomcurl
Aed Mistycrystal
Birch Toadbird"""
# split names into a list
# use each new line as delimiter
names = nameString.split('\n')

# import the random module
import random

# use the shuffle function from the random module to shuffle the names
random.shuffle(names)

# join the names together into a string, each on a new line, and print it! 
print('\n'.join(names))