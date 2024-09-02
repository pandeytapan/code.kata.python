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

The docorator executes as soon as we assign the decorator to a variable, that's why we're seeing the lines:

```bash
Running the passed function inside the decorator
This is foo...
```

However it returns the definition of the inner function and that doesn't gets executed but rather the address gets returned and assigned to the variable outside.

In the example above the `decorate` is the decorator function and the `foo` is the decorated function.

```python3
>>> from code.registration import register
registering <function f1 at 0x101dedee0> to registry
registering <function f2 at 0x101dedf80> to registry
>>> from code.registration import f1, f2, f3
>>> f1()
Running f1
>>> f2()
Running f2
>>> f3()
Running f3
>>> from code.registration import registry
>>> registry
[<function f1 at 0x101dedee0>, <function f2 at 0x101dedf80>]
>>> registry[0]
<function f1 at 0x101dedee0>
>>> registry[0]()
Running f1
>>> registry[1]()
Running f2
```
