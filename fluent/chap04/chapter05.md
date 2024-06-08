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
```

The `gulp_all` takes all the arguments packed into a tuple `args`. The syntax for this is `*args`. We can unpack and get all the arguments back as follows:

```pycon
>>> gulp_all(1, 2, "hello")
1
2
hello
```
Here is another version of the `gulp_all` that prints the type of the `args` as well as unpacks them to `print` function.

```pycon
>>> def gulp_all(*args):
...     print(type(args))
...     print(*args)
... 
>>> gulp_all(1, 2, "hello")
<class 'tuple'>
1 2 hello
```
Let's now talk about the **keyword arguments**

We have a function below named `counter` that takes two positional arguments `start` and `end`. 

```pycon
>>> def counter(start, end, delta=1):
...     for i in range(start, end, delta):
...             print(i)
...
```

Calling this function with those two arguments basically prints values frm `start` till `end`.

```
>>> counter(12, 21)
12
13
14
15
16
17
18
19
20
```

We have however one more third argument that we can pass to it *positionaly*. This argument basically defines how many numbers to skip before we print the next number in series.

```pycon
>>> counter(12, 21, 2)
12
14
16
18
20
```

This is keyword argument i.e. it has a name and a default value that is passed in case we do not supply it. 
**When an argument is passed to a function such that the argument has a name and a default value it is called as keyword argument.**
In this sense all the positional arguments are also keyword or names argument when they are passed with a name and a value.
The order of the keyword arguments doesn't matter if we are passing them with name. In the below seection we've a function `counter` that takes 4 arguments, out of which last two are provided as keyword arguments `delta` and `separator`.

```pycon
>>> def counter(start, end, delta=1, separator= ' '):
...     print(separator.join(str(i) for i in range (start, end, delta)))
... 
```

In the example below we are passing `separator` as keyword argument and this means that `delta` is passed implicitly as keyword argument.

```pycon
>>> counter(1, 11, separator = '?')
1?2?3?4?5?6?7?8?9?10
>>> counter(1, 11, separator = ' - ')
1 - 2 - 3 - 4 - 5 - 6 - 7 - 8 - 9 - 10
```
In the example below we're passing all the arguments as the keyword or named argument (see how we've rearranged their order):

```pycon
>>> counter(separator = ' - ', end = 14, delta = 2, start = 1)
1 - 3 - 5 - 7 - 9 - 11 - 13
```

We can pass the keyword arguments in any order till we're passing them as **named** arguments:

```pycon
>>> counter(1, 11, separator = ' - ', delta = 4)
1 - 5 - 9
```

However when passing them as the positional arguments we have to make sure that they're being passed according to their types

```pycon
>>> counter(1, 11, ' - ', 4)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in counter
AttributeError: 'int' object has no attribute 'join'
```

So to summerize:

- We can pass the arguments as postional arguments and the order of passing matters.
- We can pass the arguments as keyword arguments and in which case the order of passing doesn't matters.
-
## Accepting Keyword-only arguments

we saw in out last examples that arguments can be passed positionally or as keyword arguments i.e. with a name and a value. There can be however circumstances when we can pass arguments only as the keyword arguments.

The function below `greet` accepts two arguments `names` and `greeting`. The first argument accepts any number of the positional arguments and packs them into a tuple `greet`. The second argument in such cases can only be passed as a keyword-only argument.

```pycon
>>> def greet(*names, greeting):
...     for name in names:
...             print(greeting, name)
... 
```

In the code snippet below we're passing greeting as a keyword argument and thus the Python can make a clear distinction from the positional arguments.

```pycon
>>> greet('Roy', 'Mohan', greeting="Hello")
Hello Roy
Hello Mohan
```

However, if we try to pass the keyword argument as a postional argument (which is possible) then we will get an error since python now cannot differentiate between the two.

```pycon
>>> greet('Roy', 'Mohan', "Hello")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: greet() missing 1 required keyword-only argument: 'greeting'
>>> 
```

## Accepting Positional-only arguments

> Works with and beyond Python 3.8

There maybe a situation when we want all our arguments to be the positional only arguments. Consider the function definition below that is little weird.

```pycon
>>> def alphabets(start, stop=None):
...     if stop is None:
...             start, stop = 'a', start
...     print(' '.join(chr(letter) for letter in range(ord(start), ord(stop))))
... 
>>> alphabets('f')
a b c d e
>>> alphabets('q', 'x')
q r s t u v w
>>> 
```

Now this `alphabets` function works in a manner that single argument is always considered as the stop argument, whereas when two arguments are passed the first argument is always the start and the second argument is always the stop argument.

There is no point here to pass the arguments as the keyword arguments. We can modify the arguments to accept only the positonal arguments as follows

```pycon
>>> def alphabets(start, stop=None, /):
...     if stop is None:
...             start, stop = 'a', start
...     print(' '.join(chr(letter) for letter in range(ord(start), ord(stop))))
... 
>>> alphabets(start='a', stop='b')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: alphabets() got some positional-only arguments passed as keyword arguments: 'start, stop'
>>> alphabets('j')
a b c d e f g h i
```

All the arguments before the `/` are treated as the positional argument.

## Accepting some keyword and some positional arguments

We can have situation where we want some arguments to be passed positionally and some arguments to be passed as the keyword argument.

```pycon
>>> def alphabets(start, stop = None, *, sep = ' ', step = 1):
...     if stop is None:
...             start, stop = 'a', start
...     print(sep.join(chr(letter) for letter in range(ord(start), ord(stop), step)))
...
>>> alphabets("t")
a b c d e f g h i j k l m n o p q r s
>>> alphabets("k","t")
k l m n o p q r s
>>> alphabets("k","t", step=2)
k m o q s
>>> alphabets("k","t", step=2, sep= ' - ')
k - m - o - q - s
>>> alphabets("k","t", 2, ' - ')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: alphabets() takes from 1 to 2 positional arguments but 4 were given
```

## Retrieving the parameter information

The function written below accepts a parameter and clips the text at rightmost space character:

```python
def clip(text: str, max_len: int = 80):
    '''Clips a text at or before the max_len'''

    end = None
    if len(text) > max_len:
        space = text.rfind(' ', 0, max_len)
        if space >= 0: # There is a rightmost space within the range max_len
            end = space
        else: # We need ot search beyond the max_len
            space = text.rfind(' ', max_len)
            if space >=0 :
                end  = space
    if end is None:
        end = len(text)
    return text[:end].rstrip()
```
