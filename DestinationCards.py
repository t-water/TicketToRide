import csv
import random
from collections import deque

class DestinationCard:
    def __init__(self, v1, v2, score):
        self.v1 = v1
        self.v2 = v2
        self.score = int(score)

    def __str__(self):
        return self.v1 + ' -> ' + self.v2 + ' = ' + str(self.score)

class DestinationCardDeck:
    def __init__(self):
        self.__cards = deque()
        
        with open('DestinationCards.csv', newline='') as csv_file:
            card_reader = csv.reader(csv_file, delimiter=' ', quotechar='|')
            for row in card_reader:
                entries = row[0].split(',')
                self.__cards.append(DestinationCard(entries[0], entries[1], entries[2]))
        
        random.shuffle(self.__cards)
    
    def __take_cards(self, numCards):
        return [self.__cards.popleft() for _ in range(numCards)]
    
    def draw(self):
        if len(self.__cards) == 1:
            return self.__take_cards(1)
        else:
            return self.__take_cards(2)
    
    def return_card(self, card):
        self.__cards.append(card)