def make_averager():
    count = 0
    total = 0

    def averager(new_value):
        nonlocal count, total
        total += new_value
        count += 1
        return total / count

    return averager
