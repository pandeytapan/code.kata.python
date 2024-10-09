# Example that shows difference between the runtime and the rgistration time
# for a decorator.

registry = []


def register(funcptr):
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
