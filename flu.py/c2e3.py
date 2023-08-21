# The * is an amazing contender to grab those extra arguments under one name (list obviously here)
# The below is an exampel of the parallel assignment with additional elements grabbing
one, two, *rest = range(5)
print(f"One = {one}, Two = {two}, Rest = {rest}")

# Grab can occur in any position

*head, body, tail = range(5)
print(f"Head = {head}, body = {body}, tail = {tail}")
