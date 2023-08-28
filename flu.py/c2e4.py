# In this section we are going to see the slicing feature of the Python
# Slice in itself is basically a object type in the Python

s = 'Bicycle'

print(s[::1])
print(s[::-1])

# Mutable sequences can be grafted or modified with the slice notation

s = list(range(10))
print(s)

# When target assignment is a slice than the right hand side must be a slice
s[2:5] = [20, 30]
print(s)

s[2:5] = [100]
print(s)


