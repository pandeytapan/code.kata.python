# The * is an amazing contender to grab those extra arguments under one name (list obviously here)
# The below is an example of the parallel assignment with additional elements grabbing
one, two, *rest = range(5)
print(f"One = {one}, Two = {two}, Rest = {rest}")

# Grab can occur in any position

*head, body, tail = range(5)
print(f"Head = {head}, body = {body}, tail = {tail}")

# Using the named tuple
# In the example below the City is a named tuple that we can use just like a class
from collections import namedtuple
# In example below the City is namedtuple and it has four attributes
City = namedtuple('City', 'name country population coordinates')

# Now let us createa  city
tokyo = City('Tokyo', 'JP', 36.933, (35.68922, 139.69677))

# Let us now print the city
print(tokyo)

# we can access the individual attributes either using dot notation or using the index operators
print(tokyo.name)
print(tokyo.coordinates)
print(tokyo[1])
print(tokyo[2])

# named tuple has some very useful class methods that we can use thta includes 
# 1. _make() creates a namedtuple
# 2. _asdict() returns a Ordereddictionary
# 3. _fields that returns the field in the tuple
LatLong = namedtuple('LatLong', 'lat long')
# Now let us create a tuple using the LatLong named tuple
delhi_ncr = ('Delhi NCR', 'IN', 21.472, LatLong(28.613889,77.208889))

# Next we create a City type namedtuple using the delhi_ncr
delhi = City._make(delhi_ncr)
print(delhi)

# Let's get a OrderedDict out of the namedtuple
print(delhi._asdict())
