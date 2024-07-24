from functools import reduce


def factorial(num: int) -> int:
    return reduce(lambda a, b: a * b, range(1, num + 1))
