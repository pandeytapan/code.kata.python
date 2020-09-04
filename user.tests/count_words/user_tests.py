def count_words(string):
    """Return the number of times each word occurs in the string."""
    count = {}
    for word in string.split():
        if word not in count:
            count[word] = 0
        count[word] += 1
    return count

print(count_words("oh what a day what a lovely day"))

