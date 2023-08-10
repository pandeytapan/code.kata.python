# Cartesian product without listcomps

colours = ['Red', 'Black']
sizes = ['S', 'M', 'L']

for c in colours:
    for s in sizes:
        x = c,s
        print(x)
        
l = [(c,s) for c in colours for s in sizes]

print(l)
