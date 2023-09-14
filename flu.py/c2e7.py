# When list is not an answer

# In cases like where the item types are mostly homogeneous we can have array.array that is more fast and efficient
# than working with the list type

from array import array
from random import random

floats = array('d', (random() for i in range (10**5)))
print (floats [0])
print(floats [-1])

with open('floats.bin', 'wb') as f:
    floats.tofile(f)


# A memoryview is a nice way to share the same set of memory without copying the bytes

numbers = array('h', [-2, -1, 0, 1, 2])
memv = memoryview(numbers) # This creates a memoryview of the numbers type

print(memv[0])

memv_oct = memv.cast('B')
print(memv_oct.tolist())
numbers[0] = -3
print(memv[0])
