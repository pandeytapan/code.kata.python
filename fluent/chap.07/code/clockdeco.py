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
