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
