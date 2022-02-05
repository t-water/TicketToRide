import csv
from Destinations import Destinations

class DestinationCard():
    def __init__(self, v1, v2, score):
        self.v1 = v1
        self.v2 = v2
        self.score = score

destination_cards = []

with open('DestinationCards.csv', newline='') as csv_file:
    card_reader = csv.reader(csv_file, delimiter=' ', quotechar='|')
    for row in card_reader:
        entries = row[0].split(',')
        destination_cards.append(DestinationCard(Destinations[entries[0]], Destinations[entries[1]], entries[2]))