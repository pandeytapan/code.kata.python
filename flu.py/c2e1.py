# Understanding the list comprehension

# Cartesian product without listcomps

colours = ['Red', 'Black']
sizes = ['S', 'M', 'L']

for c in colours:
    for s in sizes:
        x = c,s
        print(x)
# Cartesian product using the list comprehension 
l = [(c,s) for c in colours for s in sizes]
print(l)
# list comps are suited for just one purpose. To generate a new list in one go and that's all.

# Understanding generator expression

# These are best suited when we want one element at a time and don't want to bloat the memory with huge blobs

# Creating a tuple using the generator expression

symbols = 'ÿנअ ना'
val = tuple(ord(s) for s in symbols)
print(val)
