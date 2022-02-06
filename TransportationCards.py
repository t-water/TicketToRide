from collections import Counter, deque
import random
import csv

class TransportationCardDeck:
    def __init__(self):
        self.__cards = deque()
        self.__discard_pile = deque()
        self.__flop = []
        self.__wild = 'wild'

        with open('TransportationCards.csv', newline='') as csv_file:
            card_reader = csv.reader(csv_file, delimiter=' ', quotechar='|')

            for row in card_reader:
                entry = row[0].split(',')

                self.__cards.extend([entry[0]] * int(entry[1]))
            
        random.shuffle(self.__cards)
        
        self.flop()

    def draw_card(self):
        return self.__cards.popleft()
    
    def draw_cards(self, numCards):
        return [self.draw_card() for _ in range(numCards)]
    
    def initial_draw(self):
        return self.draw_cards(2)

    def __illegal_flop(self):
        c = Counter(self.__flop)
        
        return c[self.__wild] >= 3

    def flop(self):
        while len(self.__flop) == 0 or self.__illegal_flop():
            self.__discard_pile.extend(self.__flop)
            self.__flop.clear()
            self.__flop.extend(self.draw_cards(5))
    
    def print_flop(self):
        print(self.__flop)