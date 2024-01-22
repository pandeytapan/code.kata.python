# First class objects
The functions in the Python are considered as the **first class objects**. This means that they can be:
- Passed as the function arguments.
- Can be created at the runtime.
- Assigned to a variable.
- Returned as a result of a function.

## Treating a function as an object

We have written a function `factorial` in the code file **c5e1.py**. Since the functions in the Python are first class objects we can use them as objects.

```python
def factorial(num: int) -> int:
    '''
    Returns the factorial of a number
    @param num: Number whose factorial is to be calculated
    @return: Calculated factorial of the number
    '''

    return 1 if num < 2 else num * factorial(num - 1) 
```

The code below shows how we can use the functions as the first class objects:

```bash
>>> from c5e1 import factorial
>>> print(factorial.__doc__)

    Returns the factorial of a number
    @param num: Number whose factorial is to be calculated
    @return: Calculated factorial of the number
    
>>> factorial(5)
120
>>> type(factorial)
<class 'function'>
```

Since the function is an object:
- We can get its `__doc__` attribute.
- We can use it as a callable object.
- We can check its type.

## Higher order functions

A function that takes another function as an argument or that returns another function as a result is known as a higher order function. Some of the functions that are higher order functions are `map`, `sorted` and `reduce`.
