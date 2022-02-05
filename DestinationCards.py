import csv
import random

class DestinationCard:
    def __init__(self, v1, v2, score):
        self.v1 = v1
        self.v2 = v2
        self.score = int(score)

    def __str__(self):
        return self.v1 + ' -> ' + self.v2 + ' = ' + str(self.score)

class DestinationCardDeck:
    def __init__(self):
        self.__cards = []
        
        with open('DestinationCards.csv', newline='') as csv_file:
            card_reader = csv.reader(csv_file, delimiter=' ', quotechar='|')
            for row in card_reader:
                entries = row[0].split(',')
                self.__cards.append(DestinationCard(entries[0], entries[1], entries[2]))
    
    def __remove_random_card(self):
        i = random.randrange(len(self.__cards))
        self.__cards[i], self.__cards[-1] = self.__cards[-1], self.__cards[i]

        return self.__cards.pop()
    
    def draw(self):
        return [self.__remove_random_card(), self.__remove_random_card()]