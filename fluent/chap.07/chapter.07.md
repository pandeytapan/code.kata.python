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

## When does Python executes a decorator

Python executes a decorator as soon as the decorator is defined. For decorator this is usually the **import time**. In the code below we have:

- Defined the function `registration` that is basically a decorator that appends the function address to the list `registry` and returns the decorated function that is basically the same as originally called function
- Defined three functions i.e. `f1`, `f2` and `f3` out of which first two are decorated ones.
- Whenever we are calling the decorator it initially prints what all functions it is decorating.

```python
# Example that shows difference between the runtime and the registration time
# for a decorator.

registry = []

def register (funcptr):
    print("registering %s to registry" % funcptr)
    registry.append(funcptr)
    return funcptr

# Lets now decorate two functions

@register
def f1():
    print("Running f1")

@register
def f2():
    print("Running f2")

def f3():
    print("Running f3")
```

In the code below we are importing the `register`. As we import the register from the module we also apply it to the `f1` and `f2`. The register gets executed as soon as it is imported. That is why we see the lines `registering .... `  twice since we are decorating two functions.

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

Remember that most decorators do change the passed function, replacing it with a inner function. **Code that uses the inner function almost always depends upon the closures**. Let's see the how variable scope works to understand the closures.


## Variable scope rules in Python
Consider the following function `f1` below. This function defines a local variable `a` that is passed as the parameter. It then prints the variable `a` and the vaiable `b` that is not defined anywhere in the program:

```python
>>> def f1(a):
...     print(a)
...     print(b)
... 
>>> f1(3)
3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in f1
NameError: name 'b' is not defined
```

When trying to print the variable `b` we are getting `NameError` stating that `b` is not defined anywhere, either locally in the function or globally in the program.

Now as a next step we defined `b` as a variable in the global namespace and called the function `f1` again:

```python
>>> b = 6
>>> f1(3)
3
6
```

This time as anticipated we are getting the correct values for the `a` and `b`.

Next, we've defined a function `f2` that first prints the value of `a`, `b` and further tries to assign a new value to the `b`.
This function however doesn't passes beyond the first `print` statement:

```python
>>> b = 12
>>> def f2(a):
...     print(a)
...     print(b)
...     b = 16
... 
```

This happened because when Python compiled the body of the function `f2` it decided that `b` is a local variable rather than a global variable. Thus it tries to fetch the value of the `b` from within the local environment and dicovers that `b` is not defined it is unbound.

```python
>>> f2(4)
4
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in f2
UnboundLocalError: cannot access local variable 'b' where it is not associated with a value
>>> 
```

If we want the Python interpreter to treat the `b` as global variable inspite of the assignment in the function we can redefine the function with the `b` being prefixed with `global` keyword:

```python
>>> b = 9
>>> def f2(a):
...     global b
...     print(a)
...     print(b)
...     b = 12
```

Now the execution of `f2` goes as desired:

```python
>>> f2(3)
3
9
>>> b
12
>>> b = 14
>>> b
14
>>> f2(1)
1
14
>>> b
12
```

## Closures

Let us first see the example code below that computes the average value of a ever increasing series:


