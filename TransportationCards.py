from collections import deque

from DrawPile import DrawPile    
from Flop import Flop

class TransportationCardDeck:
    def __init__(self):
        self.__cards = DrawPile()
        self.__discard_pile = deque()
        self.__flop = Flop()
    
    def initial_deal(self):
        return self.__cards.initial_deal()
    
    def can_take_turn(self):
        return True
    
    def take_turn(self):
        return self.__flop.take_turn()
