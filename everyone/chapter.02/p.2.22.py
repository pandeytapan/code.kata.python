TRIPLE_ELLIPSES = '...'
text = input("Enter any numeric value of at least 2 digits: ")

pointer = len(text) // 2
print(f"{text[:min(pointer, 3)]}...{text[max(-pointer, -3):]}")
