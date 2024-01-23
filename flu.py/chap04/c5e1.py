def factorial(num: int) -> int:
    '''
    Returns the factorial of a number
    @param num: Number whose factorial is to be calculated
    @return: Calculated factorial of the number
    '''

    return 1 if num < 2 else num * factorial(num - 1) 
