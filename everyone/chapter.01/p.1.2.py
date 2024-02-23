# the sum of the first ten positive integers, 1 + 2 + ... + 10.

# First way. Using string interpolation
print (f"Sum is: {1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10}")

# Second way. Using str () function
print (f"Sum is:" + str(1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10))

# Third way. Using str.format()
sum = 0
for i in range (11):
    sum += i

print ("Sum is: {0}".format(sum))