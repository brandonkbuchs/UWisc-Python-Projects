# This program evaluates either the area of a triangle or trapezoid and returns the values to the user.
# This variation uses try/except to validate inputs.

import sys # Imports the system module

# Function to calculate area of triangle based on user inputs.
def triangleArea():
    # Prints introductory lines.
    print "We will collect the necessary inputs to calculate a triangle\'s area."
    print "You will have four attempts to input valid numbers. \n"

    try_count = 0 # Variable for input validation
    while try_count < 4: # Checks the validity of both inputs simultaneously.
        # Start by setting the correct try_count to each loop.
        try_count += 1 # Increment the count variable, or else stuck in infinite loop.
        # Variables height and base, are both inputs.
        height = raw_input("What is the height of the triangle?>")
        base = raw_input("What is the length of the base of the triangle?>")

        try:
            height = float(height) # Convert height to float
            base = float(base) # Convert base to float.
            break # If successful, exits while loop.
        # Prints out the number of attempts remaining if input variables are not numbers.
        except: # When not valid float, returns to top of while loop. Warns of attempts remaining.
            print "You didn't enter a valid number for your inputs. You have ", 4 - try_count, " attempts remaining."
            if try_count == 4: # Exits program at threshold of 4.
                exit(1)

    area = 0.5 * height * base # Calculation of area of triangle based on inputs.

    # Summary statement of the calculation.
    print "A triangle with a height of ", height, "and base of ", base, "has an area of ", area, ". \n"

# Function to calculate trapezoid area based on input lengths.
def trapezoidArea():
    #Prints introductory lines.
    print "We will collect the necessary inputs to calculate a trapezoid\'s area."
    print "You will have four attempts to enter valid numbers. \n"

    try_count = 0 # Variable for input validation.
    while try_count < 4:
        try_count += 1 # Increment the count variable, or else stuck in infinite loop.
        # Collects the necessary variables, top_base, bottom_base and height
        top_base = raw_input("What is the length of the top base?>")
        bottom_base = raw_input("What is the length of the bottom base?>")
        height = raw_input("What is the height of the trapezoid?>")

        try: # Checks input variables are real numbers.
            top_base = float(top_base)
            bottom_base = float(bottom_base)
            height = float(height)
            break # Exits loop if all three variables are real numbers.
        except: # When not valid float, returns to top of while loop. Warns of attempts remaining.
            print "You didn't enter a valid number for your inputs. You have ", 4 - try_count, " attempts remaining."
            if try_count == 4: # If the count reaches the threshold, program exits without an error.
                sys.exit(1)

    area = ((top_base + bottom_base) / 2) * height # Area calculation of trapezoid.

    # Summary statement of the calculation.
    print "A trapezoid with top base length", top_base, "and bottom base length", bottom_base, "and a height of ", height, "has an area of ", area, ". \n"

def prereqInfo(): # Function for making choice on which shape to calculate error for, or exit.

    while True: # Enables continuous looping for multiple calculations.
    # Prints the program's introductory lines.
        print "This program calculates the areas of either a triangle or trapezoid.\n"
        print "Press 1 and enter to calculate a triangle's area. Press 2 and enter to calculate a trapezoid's area. Press 3 and enter to exit."

        area_choice = input("Enter your choice here.>") # User choice on which shape area is calculated.

        # Logic test to send program to appropriate function.
        if area_choice == 1: # Choice 1 is to calculate the area of a triangle.
            triangleArea()
        elif area_choice==2: # Choice 2 is to calculate the area of a trapezoid.
            trapezoidArea()
        else: # If the user enters an invalid choice, anything other than 1 or 2, program exits without error.
            sys.exit(1)

prereqInfo() # Starts the program.
