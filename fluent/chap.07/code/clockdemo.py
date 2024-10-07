import time

from clockdeco import clocked

@clock
def factorial (n: int) -> int:
    return 1 if n < 2 else return n * factorial(n - 1)
