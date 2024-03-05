cost_of_car = float(input("Cost of car (in USD): "))
miles_per_year = float(input("Miles driven per year: ")) 
gas_price = float(input("Gas price per gallon: "))
miles_per_gallon = float(input("Miles covered per gallon: "))
resale_value = float(input("Resale value after 5 years: "))

cost_of_driving_for_five_years = 5 * gas_price * miles_per_year

print(f"Resale value after 5 years is ${resale_value}")
print(f"Cost of running car for 5 years is {cost_of_car + cost_of_driving_for_five_years}")
