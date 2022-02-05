number_of_gallons = int(input("Available gas in car (in gallons): "))
miles_per_gallon = int(input("How many miles the car will go per gallon: "))
price_per_gallon = int(input("Price of Gas per gallon:"))

print("Price of running 100 miles is : %.2f" % ( 100 / miles_per_gallon * price_per_gallon))
print(f"The car can go {miles_per_gallon * number_of_gallons} miles")
