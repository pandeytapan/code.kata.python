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
