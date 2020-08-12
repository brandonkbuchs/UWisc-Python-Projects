# This program evaluates either the area of a triangle or trapezoid and returns the values to the user.

def triangleArea(): # Function for calculating area of a triangle, 1/2 * b * h
    # Prints introductory lines.
    print "We will collect the necessary inputs to calculate a triangle\'s area."
    print

    # User inputs for the height and base of the triangle. Both must be real numbers.
    height = input("What is the height of the triangle?>")
    base = input("What is the length of the base of the triangle?>")

    # Makes area calculation based on input received.
    area = 0.5 * height * base

    # Summary statement of the calculation.
    print "A triangle with a height of ", height, "and base of ", base, "has an area of ", area, "."


def trapezoidArea(): # Function for calculating the area of a trapezoid, (a + b) /2 * h
    # Prints introductory lines.
    print "We will collect the necessary inputs to calculate a trapezoid\'s area."
    print

    # Collects the necessary variables, top_base, bottom_base and height as real numbers.
    top_base = raw_input("What is the length of the top base?>")
    bottom_base = raw_input("What is the length of the bottom base?>")
    height = raw_input("What is the height of the trapezoid?>")

    # Makes area calculation based on input received.
    area = ((top_base + bottom_base) / 2) * height

    # Summary statement of the calculation.
    print "A trapezoid with top base length", top_base, "and bottom base length", bottom_base, "and a height of ", height, "has an area of ", area, "."

while True: # Enables continuous looping for multiple calculations.
    # Prints the program's introductory lines.
    print "This program calculates the areas of either a triangle or trapezoid."
    print
    print "Press 1 and enter to calculate a triangle's area. Press 2 and enter to calculate a trapezoid's area. Press 3 and enter to exit."

    area_choice = input("Enter your choice here.>") # User choice on which shape area is calculated.

    # Logic test to send program to appropriate function.
    if area_choice == 1: # Choice 1 is to calculate the area of a triangle.
        triangleArea()
    elif area_choice==2: # Choice 2 is to calculate the area of a trapezoid.
        trapezoidArea()
    else: # If the user enters an invalid choice, anything other than 1 or 2, program exits without error.
        exit(1)
