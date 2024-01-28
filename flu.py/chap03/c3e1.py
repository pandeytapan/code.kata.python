# A dictionary created using the comprehension
# We've a list of tuples that contains the dial code

from collections.abc import Mapping

DIALCODE = [
    ( 91,'India'),
    ( 1, 'United States'),
    (81, 'Japan'),
    (7, 'Russia'),
    (92, 'Pakistan')
]

# Here is how we will use the dictionary comprehension for this

country_codes = {k:v for k,v in DIALCODE}
print(country_codes)

# The dict in builtin module is derived from the ABCs 
# ABCs thus by far serve the purpose of say as checking the instance type as below
print(isinstance(country_codes, Mapping))

# The userdict and the Ordereddict are derived from the dict itself.
total_countries = {k:v for k,v in enumerate(DIALCODE)}
print(total_countries)

# We have two more mapping types coming out of the collections 
# these are defaultdict and the orderedDict

# When the key is missing in the dictionary that time we can use the default argument for the dictionary
try:
    print(country_codes[45])
except KeyError as e:
    print("Cannot find key", e)
# instead of the code above we can use get()with default argument
print(country_codes.get(45, 'Unexplored'))

