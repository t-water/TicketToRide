from collections import deque
import random
import csv

class DrawPile:
    def __init__(self):
        self.__cards = deque()
        self.__wild = 'wild'

        with open('TransportationCards.csv', newline='') as csv_file:
            card_reader = csv.reader(csv_file, delimiter=' ', quotechar='|')

            for row in card_reader:
                entry = row[0].split(',')

                self.__cards.extend([entry[0]] * int(entry[1]))
            
        random.shuffle(self.__cards)
    
    def draw_card(self):
        return self.__cards.popleft()
    
    def draw_cards(self, numCards):
        return [self.draw_card() for _ in range(numCards)]
    
    def initial_deal(self):
        return self.draw_cards(2)