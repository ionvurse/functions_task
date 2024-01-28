"""A program that uses functions to calculate the total cost of a holiday
based on the flight, accommodation and car rental costs."""

def destination():
    """Destination menu"""
    print("Please choose your preferred destination:")
    print("London")
    print("Paris")
    print("Vienna")
    print('q')

def hotel_cost(num_nights, hotel_price = 54):
    """ Function that calculates the total cost for the
    hotel stay"""
    x = num_nights * hotel_price
    return x

def car_rental(rental_days, day_price = 44):
    """Function that calculates the total cost for car rental"""
    y = rental_days * day_price
    return y

def holiday_cost(a, b):
    total = a + b
    return total

def plane_cost(choice,):
    pass
destination()
num_nights = input("How many nights do you want to stay at the hotel?: ")
num_nights = int(num_nights)
rental_days = input("How many days do you want to rent the vehicle for?: ")
rental_days = int(rental_days)
choice = 'x'
final_print = "The total cost of this holiday will be:"
print(f"The hotel stay for {num_nights} nights will cost £{str(hotel_cost(num_nights))}\n")
print(f"Renting the car for {rental_days} days will cost £{str(car_rental(rental_days))}\n")
print(f"{final_print} £{str(holiday_cost(hotel_cost(num_nights), car_rental(rental_days)))}")