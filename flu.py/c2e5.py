# Working with the + and * operators
# Using * with nested lists can be a harmful option

# To concatenate a sequence we need to multiply it 

l = [1, 2, 3, 4, 5, ' ']
l = l * 5
print(l)

s = 'abcd '
s = s * 4
print(s)

# The code below doesn't creates self references to the inner list

board = [['-'] * 3 for _ in range(3)]
print(board)
board[0][1] = 'x'
print(board)
print()

# However the code below creates a self reference to the inner list. We're trying to be smarter but getting dumb
board = [['-'] * 3] * 3
print(board)
board[0][1] = 'x'
print(board)

# The unexpected result

t = (1, 2, [3, 4])
t[2] += [5, 6]
print(t)
