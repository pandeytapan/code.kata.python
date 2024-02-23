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

Here is an example how we can pass the `factorial` to the `map` and get a list of first `n` factorials:

```bash
>>> list(map(factorial, range(10)))
[1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
```

`map` takes the address of the `factorial` and applies it to each item in the `range`.

The next example shows how we can sort a list of words by their length using the `sorted` function:

```bash
>>> fruits = ['apple', 'pineapple', 'guava', 'cherry', 'orange', 'banana', 'dragonfruit', 'custard apple']
>>> sorted(fruits, key=len)
['apple', 'guava', 'cherry', 'orange', 'banana', 'pineapple', 'dragonfruit', 'custard apple']
```

Any function that takes a single argument can be passed as the `key` here. This can be useful to keep same type of the fruits together. If we want to keep the *apple* types together we can design a `reversed` function that take a single argument that is the fruit name and returns its reversed.

We are not going to store the reversed fruit name but instead we will use it in the sorting.

```bash
>>> fruits = ['apple', 'pineapple', 'guava', 'cherry', 'orange', 'banana', 'dragonfruit', 'custard apple']
>>> def reversed(fruit:str)->str:
...     return fruit[::-1]
... 
>>> reversed("apple")
'elppa'
>>> sorted(fruits, key=reversed)
['banana', 'guava', 'orange', 'apple', 'custard apple', 'pineapple', 'dragonfruit', 'cherry']
```

## Modern Python replacement for some of the higher order functions

With the introduction of the **list comprehension** and the **set comprehension** we can replace the `map`:

```bash
>>> from c5e1 import factorial
>>> list(map(factorial, range(5)))
[1, 1, 2, 6, 24]
>>> [factorial(i) for i in range(5)]
[1, 1, 2, 6, 24]
```

## Anonymous functions

The `lambda` keyword is basically an syntatic suger that creates a function just liek how we do with the `def` keyword.
