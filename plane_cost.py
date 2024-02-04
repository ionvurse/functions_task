def destination():
    """Prints the destination menu"""
    print("Please choose your preferred destination:\n")
    print("1: London (£45),\n")
    print("2: Paris (£55),\n")
    print("3: Vienna (£65).\n")
# city_flight - user input
destination()
city_flight = input("Enter the destination city: ")
city_flight = city_flight.lower()
while not city_flight.isalpha():
    city_flight = input("Enter the destination city: ")
# else:
city_flight  = city_flight.lower()
    

# print(city_flight)
# plane_cost - function - takes city_flight as an argument and returns
# a cost of the flight - use conditonal statement in function's body
def plane_cost(x):
    """ Returns the flight price depending
    on the chosen destination"""
    if x == "london":
        return 45
    elif x == "paris":
        return 55
    elif x == "vienna":
        return 65

# a = plane_cost(city_flight)
# print(a)