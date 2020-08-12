# the multiplication of the first ten positive integers, 1 * 2 * ... * 10.

# First way. Using string interpolation
print (f"Multiplication is: {1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10}")

# Second way. Using str () function
print (f"Multiplication is:" + str(1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10))

# Third way. Using str.format()
mult = 1
for i in range (1, 11):
    mult *= i

print ("Multiplication is: {0}".format(mult))