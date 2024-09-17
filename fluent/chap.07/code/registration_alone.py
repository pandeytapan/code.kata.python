# Example that shows difference between the runtime and the rgistration time
# for a decorator.

registry = []


def register(funcptr):
    print("registering %s to registry" % funcptr)
    registry.append(funcptr)
    return funcptr
