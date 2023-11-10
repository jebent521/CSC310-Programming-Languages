from itertools import product
from random import shuffle
values = ['A', *list(range(2, 11)), 'J', 'Q', 'K']
suits = ['S', 'C', 'H', 'D']
deck = list(product(values, suits))

class Shoe:
    def __init__(self, k: int):
        '''Fills and shuffles a shoe with k decks of cards'''
        if not(isinstance(k, int) and k > 0):   # ensure k is a positive integer
            raise ValueError('k must be a positive integer!')
        self.cards = deck * k                   # fill shoe with k decks of cards
        shuffle(self.cards)                     # shuffle the shoe

    def __next__(self):
        if len(self.cards) == 0:                # stop iterating if no more cards
            raise StopIteration
        return self.cards.pop()                 # remove card from back of Shoe
    
    def __iter__(self):
        return self
    
    def __repr__(self):
        hex_address = '0x'+hex(id(self))[2:].zfill(16).upper()
        return f'<Shoe object at {hex_address}>'

