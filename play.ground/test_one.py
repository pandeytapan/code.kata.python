from operator import length_hint


class LengthHinter:
    def __init__(self, items, hinted_length):
        self.length = hinted_length
        self.items = items

    def __iter__(self):
        yield from self.items

    def __length_hint__(self):
        return self.length


def total_length(*iterables, use_hints=False):
    length = 0
    for iterable in iterables:
        try:
            length += len(iterable)
        except TypeError:
            hint = length_hint(iterable)
            if use_hints and hint:
                length += hint
            else:
                length += sum(1 for _ in iterable)
    return length


things = LengthHinter([1, 2], 10)
things2 = LengthHinter([100, 50, 20, 30, 10], 0)

print(total_length(things2, things2, use_hints=True))

