import random
import csv

class TransportationCardDeck:
    def __init__(self):
        self.__cards = []
        self.__discard_pile = []

        with open('TransportationCards.csv', newline='') as csv_file:
            card_reader = csv.reader(csv_file, delimiter=' ', quotechar='|')

            for row in card_reader:
                entry = row[0].split(',')

                self.__cards.extend([entry[0]] * int(entry[1]))
            
            random.shuffle(self.__cards)

    def draw_card(self):
        return self.__cards.pop(0)
    
    def initial_draw(self):
        return [self.draw_card(), self.draw_card()]