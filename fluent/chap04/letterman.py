def alphabets(start, stop=None, *, step=1, sep=' '):
    '''prints a series of alphabets between a range'''

    if stop is None:
        start, stop = 'a', start

    print(sep.join(chr(i) for i in range(ord(start), ord(stop), step)))
