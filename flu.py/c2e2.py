# A tuple is not merely a "immutable list" but rather it is a way to record the columns in vital order

lax_coordinates = 33.9425, -118.408056
city, year, pop, chg, area = 'Tokyo', 2003, 32450, 0.66, 8014
traveler_ids = [('USA','31195855'), ('BRA', 'CE243567'), ('ESP', 'XDA205856')]

# In the code below the passport is assigned a tuple
for passport in sorted(traveler_ids):
    # A tuple has its columns indexed numerically from zero
    print(f'{passport[0]} - {passport[1]}')
    # A tuple can also be unpacked if required
    country, pass_id = passport
    print(f'{country} - {pass_id}')
