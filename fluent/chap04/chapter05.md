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

```pycon
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

```pycon
>>> list(map(factorial, range(10)))
[1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
```

`map` takes the address of the `factorial` and applies it to each item in the `range`.

The next example shows how we can sort a list of words by their length using the `sorted` function:

```pycon
>>> fruits = ['apple', 'pineapple', 'guava', 'cherry', 'orange', 'banana', 'dragonfruit', 'custard apple']
>>> sorted(fruits, key=len)
['apple', 'guava', 'cherry', 'orange', 'banana', 'pineapple', 'dragonfruit', 'custard apple']
```

Any function that takes a single argument can be passed as the `key` here. This can be useful to keep same type of the fruits together. If we want to keep the *apple* types together we can design a `reversed` function that take a single argument that is the fruit name and returns its reversed.

We are not going to store the reversed fruit name but instead we will use it in the sorting.

```pycon
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

```pycon
>>> from c5e1 import factorial
>>> list(map(factorial, range(5)))
[1, 1, 2, 6, 24]
>>> [factorial(i) for i in range(5)]
[1, 1, 2, 6, 24]
```

## Anonymous functions

The `lambda` keyword is basically an syntatic suger that creates a function just like how we do with the `def` keyword.

## The callable ones

Whenever any user-defined type has `()` operator defined for itself, then it is known as callable type. Callable type is something that can be called as a function. Following are the callable types and ways in which we can create them:

- **User defined functions**: Theses are defined using the `def` keyword or the `lambda` expressions.
- **Builtin functions**: These are the ones that are implemented in the C (like `len` etc.)
- **Builtin methods**: Again implemented in the C (like dict.get)
- **Methods**: Functions that are defined in the body of a class.
- **Classes**: They when invoked with `()` first call the `__new__` followed by the `__init__` to create and return an instance.
- **Class instances**: When the class defines `__call__` then its instances can be invoked as functions.
- **Generator functions**: Functions that use the `yield` keyword.

## Creating a user-defined callable type

We can make arbitrary python objects to behave as a function. All it requires is implementation of the `__call__` method.
Below we have is a class named `Bingo` that implements `__call__` and thus can be directly called as function (*see `bingoit()`*)

```python

import random


class Bingo:
    '''
    Bingo is an example of the user defined callable type.
    It implements __call__ that allows it to make it a callable type.
    '''

    def __init__(self, items):
        self._items = list(items)  # Make a copy of the passed iterable
        random.shuffle(self._items)

    def pick(self):
        '''
        Main method of the Bingo using which we can pick any random element
        '''
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError("Pick from empty Bingo Cage.")

    def __call__(self):
        '''
        Makes Bingo a callable.
        With this implementation we can call Bingo as a function
        '''
        return self.pick()
```

To use the the `Bingo` as a object:

```pycon
>>> from bingo import Bingo
>>> bingoit = Bingo(range(20))
>>> bingoit.pick()
15
>>> bingoit()
4
>>>
```

## Introspection of functions

If we look at the attributes of the function using te `dir()` we can see that there are many attributes for a function:

```pycon
>>> dir (factorial)
['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
>>>
```

We can however add new attributes to the functions as required (though it is not a common practice)

```bash
>>> factorial.__doc__
'\n    Returns the factorial of a number\n    @param num: Number whose factorial is to be calculated\n    @return: Calculated factorial of the number\n    '
>>> factorial.what_you_do = "I can calculate factorial for any integer."
>>> dir(factorial)
['__annotations__', '__builtins__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__getstate__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'what_you_do']
>>> factorial.what_you_do
'I can calculate factorial for any integer.'
>>>
```

## The positional and the keyword arguments

In Python we can write function to which we can pass any number of the arguments *positionally*. This means basically writing the arguments as they come.
Here is example of a function that takes all the arguments positionally:

```pycon
>>> def gulp_all(*args):
...     for arg in args:
...             print(arg)
... 
>>> gulp_all(1, 2, "hello")
1
2
hello
>>> def gulp_all(*args):
...     print(type(args))
...     print(*args)
... 
>>> gulp_all(1, 2, "hello")
<class 'tuple'>
1 2 hello
```
