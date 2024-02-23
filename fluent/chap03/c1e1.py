# Example of a Pythonic card deck
from collections import namedtuple

# A named tuple can be used to create a tuple like class
Card = namedtuple('Card', ['rank', 'suit'])

# Value of the suit
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

# let us now create a french deck based on the deck


class french_deck:
    ranks = [position for position in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    # initialize the french deck
    # _cards is basically a list of Card type
    def __init__(self):
        self._cards = [Card(rank, suit)
                       for suit in self.suits
                       for rank in self.ranks]

    # Get the total number of cards in the deck
    def __len__(self):
        return len(self._cards)

    # Get the card at a particular position
    # We basically are returning particular item from the list
    # with __getitem__ implemented we can now support the slicing also
    # The `in` operator requires __contains__, but in case it is not there
    # it uses __getitem__ and traverses sequentially.
    def __getitem__(self, pos):
        return self._cards[pos]

# Function to rank each of the individual card in the suit


def card_rank(some_card):
    rank_of_card = french_deck.ranks.index(some_card.rank)
    rank_of_card = rank_of_card * \
        len(suit_values) + suit_values[some_card.suit]
    return rank_of_card
