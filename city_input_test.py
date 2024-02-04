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

# print(city_flight)