# This program calculates the area of a triangle.

# These two print statements print out the program purpose and new line.
print "This program finds the area of a triangle."
print

# There are two variables, height and base, which ask for inputs from the user. The variable must be a number.
height = input("Please enter the height of the triangle: ")
base = input("Please enter the base length of the triangle: ")

# The variable, area, is calculated as 0.5 times the two other variables, height and base.
area = 0.5 * height * base

# Prints a statement describing the variables height, base, and area in common phrases.
print "The area of a triangle with height", height, "and base", base, "is", area, "."
