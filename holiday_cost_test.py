def holiday_cost(a, b, c):
    """Calculates the holiday's total cost"""
    holiday_total = a + b + c
    return holiday_total

# main
city_flight = 45
nights_total = 200
car_rent = 350

print(holiday_cost(city_flight, nights_total, car_rent))