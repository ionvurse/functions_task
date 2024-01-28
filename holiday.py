"""A program that uses functions to calculate the total cost of a holiday
based on the flight, accommodation and car rental costs."""

def hotel_cost(num_nights, hotel_price = 54):
    """ Function that calculates the total cost for the
    hotel stay"""
    x = num_nights * hotel_price
    return x

def destination():
    """Destination menu"""
    print("Please choose your preferred destination:")
    print("London")
    print("Paris")
    print("Vienna")

destination()
num_nights = input("How many nights do you want to stay at the hotel?: ")
num_nights = int(num_nights)
rental_days = input("How many days do you want to rent the vehicle for?: ")
rental_days = int(rental_days)
choice = 'x'

print(f"The hotel stay for {num_nights} nights will cost you £{str(hotel_cost(num_nights))}")
