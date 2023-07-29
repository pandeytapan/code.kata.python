# Example of a Pythonic card deck
from collections import namedtuple

# A named tuple can be used to create a tuple like class
Card = namedtuple('Card', ['rank', 'suit'])

# let us now create a french deck based on the deck

class french_deck:
    ranks = [position for position in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    # initialize the french deck
    # _cards is basically a list of Card type
    def __init__(self):
        self._cards = [Card(rank,suit) 
                       for suit in self.suits 
                       for rank in self.ranks]
    
    # Get the total number of cards in the deck
    def __len__(self):
        return len(self._cards)

    # Get the card at a particular position
    # We basically are returning particular item from the list
    def __getitem__(self, pos):
        return self._cards[pos]
