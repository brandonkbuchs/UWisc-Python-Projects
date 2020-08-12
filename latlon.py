# This program collects latitude and longitude inputs from the user and returns
# Information on the location of the quadrant of the coordinate provided
def latlon(latitude, longitude): # Defines function
    # Latitude logic tests.
    if latitude == 0: # Test if on equator
        print "That location is on the equator."
    elif latitude > 0 and latitude <= 90: # Test if north of equator
        print "That location is north of the equator."
    elif latitude < 0 and latitude >= -90: # Test if south of equator.
        print "That location is south of the equator."
    elif latitude < -90 or latitude > 90: # Invalid entry.
        print "That location does not have a valid latitude!"

    # Longitude logic tests.
    if longitude == 0: # Test if prime meridian
        print "That location is on the prime meridian."
    elif longitude > 0 and longitude <= 180: # Tests if east of PM.
        print "That location is east of the prime meridian."
    elif longitude < 0 and longitude >= -180: # Tests if west of PM.
        print "That location is west of the prime meridian."
    elif longitude < -180 or longitude > 180: # Invalid entry.
        print "That location does not have a valid longitude!"

while True:
    # Print instructions to the user.
    print "This program will tell you where latitude and longitude fall on the Earth."
    print "Please follow the instructions. Enter only real numbers."
    print "Latitude must be a number between -90 and 90."
    print "Longitude must be a number between -180 and 180.\n"

    latitude = raw_input("Enter your latitude here.>") # Latitude variable
    longitude = raw_input("Enter your longitude here.>") # Longitude variable

    try: # Test whether input is real number.
        latitude = float(latitude)
        longitude = float(longitude)
        break
    except: # Prints error message, restarts program for all non-real numbers.
        print "Please enter a valid number for both latitude and longitude."

latlon(latitude, longitude) # Calls function
