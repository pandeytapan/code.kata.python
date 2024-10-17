import time

from clockdeco import clock

@clock
def factorial (n: int) -> int:
    return 1 if n < 2 else n * factorial(n - 1)
