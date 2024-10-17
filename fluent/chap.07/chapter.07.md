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

```python
class Averager():
    def __init__(self):
        self.series = []

    def __call__(self, value):
        self.series.append(value)
        return sum(self.series)/len(self.series)
```

So in the code above we have created an attribute `series` that stores the number in the series and we have overloaded the dunder `__call__` to make it a callable.

**Now we're going to do the same thing with a higher order function**


A **higher-order function** is a function that either takes one or more functions as arguments or returns a function as its result. In that sense all the decorators that we've define are basically higher order function, as they take a function as an argument and return a function as a result.

A **closure is a function** that *captures the lexical scope** in which it was created. This means that a closure remembers the environment where it was defined, even when it is executed outside that scope. Closures are often used in conjunction with higher-order functions.

Now lets create the `Averager` using a functional approach:

```python
def make_averager():
    series = []

    def averager(value):
        series.append(value)
        return sum(series) / len(series)

    return averager
```

The `averager` in the code above is returned back during the call to the `make_averager`. We can make use of the returned function `avg` just like the way we did in last example:

```python
>>> from average_closure import make_averager
>>> avg = make_averager()
>>> avg(10)
10.0
>>> avg(11)
10.5
>>> avg(12)
11.0
>>> avg(13)
11.5
```

It is worth to understand how this time `avg` manages the series of the numbers. In the last example where we used the class we have `series` maintained as a attribute. 

This time we have `series` defined and maintained as local variable of the function `make_averager`. Now when we are calling `avg`, we are actually calling the `averager` and `make_average` is already gone back. Comes question how we're accessing the `series` inside the `average`.

Within the `averager` the `series` is known as the free variable i.e. a variable that is not bound to the local scope but is equally accessible in that scope.

All the local and the free variables are kept under the `__code__` attribute that actually represents the compiled body of the function:

```python
>>> from average_closure import make_averager
>>> avg = make_averager()
>>> avg(10)
10.0
>>> avg.__code__.co_varnames
('value',)
>>> avg.__code__.co_freevars
('series',)
```

So, closures have free variable, this means a set of variables that are out of scope for closure but are accessible within the closure. Closure retains the binding to the free variables that can be used later when the function has returned.

We can make the code for the `averager` a bit better by removing the `series` list and instead keeping the sum and computing the average like this:

```python
def make_averager():
    count = 0
    total = 0

    def averager(new_value):
        total += new_value
        count += 1
        return total / count

    return averager
```

And now we can call the function like this:

```python
>>> avg = make_averager()
>>> avg(10)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    total += new_value
    ^^^^^
UnboundLocalError: cannot access local variable 'total' where it is not associated with a value
```

So, again we're getting the `UnboundLocalError`, and this is because whenever we access the immutable values like integers, lists or the tuples this is considered as accessing a variable even before it is declared. This is equally same as accessing a global variable inside a function without even giving it the global declaration.

we can correct the code as follows:

```python
def make_averager():
    count = 0
    total = 0

    def averager(new_value):
        nonlocal count, total
        total += new_value
        count += 1
        return total / count

    return averager
```

And now when we'll run the code we will get the result:

```python
>>> avg = make_averager()
>>> avg(10)
10.0
>>> avg(11)
10.5
```

## Creating a simple decorator in the Python

So as per our last discussion we saw that closures are a way to bound veriables out of scope as well as returning an inner function that completely replaces the definiton of function to what it is assigned.

- Remember that decorator takes a function as an argument and completely replaces it with a new function.
- Decorator basically follows the rule of the closure and relies on the free variable concept to get access to variables defined outside the scope.

In the example below we've defined a decorator `clock` that basically shows how much time it took to execute a function:

```python
import time

def clock(funcptr):
    '''
    The clock decorator calculates how much time it takes to execute a function
    @param funcptr: The decorated function
    '''

    def clocked(**args):
        '''
        Clocked is the inner function that is the replacement for the funcptr
        Arguments passed to the funcptr are actually captured in the clocked
        '''
        
        t0 = time.perf_counter()
        result = funcptr(*args)
        t1 = time.perf_counter() - t0
        name = funcptr.__name__
        arg_str = ','.join(repr(arg) for arg in args)
        print("[%0.8f] %s(%s) -> %r" % (t1, name, arg_str, result))

        return result

    return clocked
```

In the line `result = funcptr(*args)`, we're able to access the `args` only because closure is having access to the free variable.

Here is the example below how we can use the `clocked`:

```python
>>> from clockdeco import clock
>>>
>>> @clock
... def factorial(n: int) -> int:
...     return 1 if n < 2 else n * factorial(n -1)
...
>>> factorial(6)
[0.00000125] factorial(1) -> 1
[0.00005714] factorial(2) -> 2
[0.00007815] factorial(3) -> 6
[0.00009683] factorial(4) -> 24
[0.00011541] factorial(5) -> 120
[0.00013862] factorial(6) -> 720
720
```

This is typical behaviour of a decorator. It replaces the decorated function with a new definition. It however *usually* accepts the same arguments as passed to the original function and returns the same value as by original function. 

There is however a problem with the decorator `clock` that we've written. It basically masks the `__name__` and `__doc__` attribute of the decorated function `factorial`:

```python
>>> factorial.__name__
'clocked'
>>> factorial.__doc__
'\n        Clocked is the inner function that is the replacement for the funcptr\n        Arguments passed to the funcptr are actually captured in the clocked\n
```

## Using the `functools`

The `functools` module of the standard library provides various tools for decorator writing. Using the `wraps` docorator we can easily handle the shortcomings in the last example. Here is the updated version of the `clock` decorator:

```python
import time
import functools


def clock(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs)
        t1 = time.time() - t0
        args_list = []
        # If there are any args or kwargs we can add them into the display list
        if args:
            args_list.append(', '.join(repr(arg) for arg in args))
        if kwargs:
            pairs = [("%s=%s" % (k, v) for k, v in sorted(kwargs.items()))]
            args_list.append(', '.join(pairs))
        arg_str = ','.join(args_list)

        print("[%0.8fs] %s -> %r" % (t1, arg_str, result))
        return result
    return clocked
```

This time when we run the program we will get the actual unmasked values:

```python
>>> @clock
... def factorial(n):
...     '''Returns the factorial of a given number'''
...     return 1 if n < 2 else n * factorial (n - 1)
...
>>> factorial(4)
[0.00000191s] 1 -> 1
[0.00006700s] 2 -> 2
[0.00008869s] 3 -> 6
[0.00011492s] 4 -> 24
24
>>> factorial.__name__
'factorial'
>>> factorial.__doc__
'Returns the factorial of a given number'
```
