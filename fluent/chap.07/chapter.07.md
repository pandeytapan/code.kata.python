# Function decorators and closures

Function decorators allow us to mark the functions in the source code in some way to enhance their working.

## Decorator 101

Decorator is a function that takes another function as an argument and:

- performs some processing with the passed function.
- can return it or replaces it with the another function.

So, lets say we have an existing function named `decorate` and it can take another function as argument then:

```python
def target():
    print("Running target")

target = decorate(target)
```

is same as:

```python
@decorate
def target():
    print("Running target")
```

So let's now write the definition of our decorator `decorate` and see how it replaces the original function:

```python
def decorate(func):
    print("Running original function inside the decorator")
    func()
    def inner():
        print("Running inner")
    return inner
```

and here is the sample run of decoration:

```bash
>>> from decorator import decorate
>>> def foo():
...     print("This is foo...")
...
>>> foo = decorate(foo)
Running the passed function inside the decorator
This is foo...
>>> foo()
The inner function
```

