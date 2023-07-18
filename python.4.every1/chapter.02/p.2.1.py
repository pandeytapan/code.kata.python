# Program that displays dimensions of a letter sheet in millimeters
INCH_IN_MM = 25.4

length = float(input("Enter length in inches: "))
breadth = float(input("Enter breadth in inches: "))

# We can use the string interpolation
print(f"{length} in x {breadth} in = {length * INCH_IN_MM} mm x {breadth * INCH_IN_MM} mm")

# Using format specifier is a good reason here
print("%.2f in x %.2f in = %.2f mm x %.2f mm" %(length, breadth, length * INCH_IN_MM, breadth * INCH_IN_MM))
