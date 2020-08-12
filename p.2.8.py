from math import sqrt

side_A = float(input("Ente side A:"))
side_B = float(input("Ente side B:"))

print("Area of Rectangle : %.2f" % (side_A * side_B))
print("Perimeter of Rectangle : %.2f" % (2 * (side_A + side_B)))
print("Length of diagonal : %.2f" % (sqrt(side_A ** 2 + side_B ** 2)))

