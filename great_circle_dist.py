import math # Import Python's math module for use

# This program calculates the distance between two coordinate points on the earth.

print "This program calculates the distance between two cities, provided coordinates in decimal degrees. \n"
city_a = raw_input("Enter the origin city here.>") # First city from user
city_b = raw_input("Enter destination city here.>") # Second city

# Test for valid coordinate systems
while True:
    print "Enter the coordinates in decimal degrees.\n"
    latitude_a = raw_input("Enter latitude for origin city.>")
    longitude_a = raw_input("Enter the longitude for origin city.>")
    latitude_b = raw_input("Enter the latitude for the destination city.>")
    longitude_b = raw_input("Enter the longitude for the destination city.>")

    try: # Validate input as real number for each coordinate entered.
        latitude_a = float(latitude_a)
        longitude_a = float(longitude_a)
        latitude_b = float(latitude_b)
        longitude_b = float(longitude_b)
        break
    except: # Print error message if coordinates are not valid
        print "Enter valid coordinates in the field."

degrees = [latitude_a, latitude_b, longitude_a, longitude_b] # List to iterate over lat/longs.
radians = [] # List for coordinates in radians, converted below.

for i in degrees: # Iterate over each coordinate and convert to radians.
    i = math.radians(i)
    radians.append(i)

# Building distance equation
lat_sin = math.sin(radians[0]) * math.sin(radians[1])
lat_cos = math.cos(radians[0]) * math.cos(radians[1])
long_cos = math.cos(radians[2] - radians[3])
distance = math.acos(lat_sin + lat_cos * long_cos) * 6300 # Multiply by spherical distance
# distance = round(distance, 0) # Round the distance to avoid long floats.
distance = round(distance,0) # Rounds the distance
distance = int(distance) # Removes floating decimal for clean integer
# Prints distance in neat format.
print "Origin:", city_a, "Destination:", city_b, "Distance:", distance, "km."
