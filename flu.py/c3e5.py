# A python example of the set operations

fruits = {
    'apple', 'banana', 'cherry', 'date', 'elderberry',
    'fig', 'grape', 'honeydew', 'kiwi', 'lemon',
    'mango', 'orange', 'papaya', 'quince', 'raspberry',
    'strawberry', 'tangerine', 'watermelon', 'blueberry', 'cranberry',
    'guava', 'lime', 'pear', 'pineapple', 'plum',
    'apricot', 'blackberry', 'cantaloupe', 'coconut', 'grapefruit'
}
fruits_subset = {
    'apple', 'banana', 'cherry', 'date', 'elderberry',
    'fig', 'grape', 'honeydew', 'kiwi', 'lemon'
}

print(len(fruits&fruits_subset))

