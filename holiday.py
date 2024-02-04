"""A program that uses functions to calculate the total cost of a holiday
based on the flight, accommodation and car rental costs."""

def plane_cost(flight):
    """ Returns the flight price depending on the chosen destination.
    
    parameter: chosen destination as string

    returns: integer value based on if/else conditional"""

    if flight == "london":
        return 45
    elif flight == "paris":
        return 55
    elif flight == "vienna":
        return 65

def hotel_cost(hotel, hotel_price = 54):
    """Calculates the total cost for the
    hotel stay

    parameters: input number of nights and default price value

    returns the multiplication result of passed arguments"""

    hotel_total = hotel * hotel_price
    return hotel_total

def car_rental(car, day_price = 44):
    """Calculates the total cost for car rental

    parameters: input number of renal days and default price value

    returns the multiplication result of passed arguments"""

    car_total = car * day_price
    return car_total

def holiday_cost(a, b, c):
    """Calculates the holiday's total cost"""
    holiday_total = a + b + c
    return holiday_total

def destination():
    """Destination menu"""
    print("Please choose your preferred destination:\n")
    print("1: London (£45),\n")
    print("2: Paris (£55),\n")
    print("3: Vienna (£65).\n")

dot_line_delimiter = "-" * 80

city_flight_list = ["london", "paris", "vienna"]
print("\nLet's calculate the cost of your holiday:\n")

destination()
city_flight = input("\nEnter the destination city: ").lower()


while city_flight not in city_flight_list:
    print("\nEnter the name of the city you want to fly to.")
    city_flight = input("Enter the destination city: ").lower()


print(dot_line_delimiter)

num_nights = input("\nHow many nights do you want to stay at the hotel?: ")
while not num_nights.isnumeric():
    print("\nPlease enter a number (digit).")
    num_nights = input("How many nights do you want to stay at the hotel?: ")
num_nights = int(num_nights)

print(dot_line_delimiter)

rental_days = input("\nHow many days do you want to rent the vehicle for?: ")
while not rental_days.isnumeric():
    print("\nPlease enter a number (digit).")
    rental_days = input("How many days do you want to rent the vehicle for?: ")
rental_days = int(rental_days)

print(dot_line_delimiter)

flight_print = "The cost of the flight to "
hotel_print = "The hotel stay for "
car_print = "Renting the car for "
final_print = "The total cost of this holiday will be:"

print(f"""\n{flight_print}{city_flight.capitalize()} is £{str(plane_cost(city_flight))}\n
{dot_line_delimiter}""")
print(f"""\n{hotel_print}{num_nights} nights will cost £{str(hotel_cost(num_nights))}\n
{dot_line_delimiter}""")
print(f"""\n{car_print}{rental_days} days will cost £{str(car_rental(rental_days))}\n
{dot_line_delimiter}""")
print(f"""\n{final_print} £{str(holiday_cost(hotel_cost(num_nights),
                         car_rental(rental_days), plane_cost(city_flight)))}\n{dot_line_delimiter}\n""")