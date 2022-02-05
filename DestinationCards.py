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

# DESTINATION_CARDS = [
#     DestinationCard(Destinations.PICCADILLY_CIRCUS, Destinations.BRITISH_MUSEUM, 2),
#     DestinationCard(Destinations.HYDE_PARK, Destinations.COVENT_GARDEN, 3),
#     DestinationCard(Destinations.PICCADILLY_CIRCUS, Destinations.WATERLOO, 3),
#     DestinationCard(Destinations.TRAFALGAR_SQUARE, Destinations.THE_GLOBE_THEATRE, 4),
#     DestinationCard(Destinations.THE_GLOBE_THEATRE, Destinations.BRICK_LANE, 4),
#     DestinationCard(Destinations.BRITISH_MUSEUM, Destinations.ST_PAULS, 4),
#     DestinationCard(Destinations.BRITISH_MUSEUM, Destinations.WATERLOO, 4),
#     DestinationCard(Destinations.TRAFALGAR_SQUARE, Destinations.ST_PAULS, 4),
#     DestinationCard(Destinations.BIG_BEN, Destinations.THE_CHARTERHOUSE, 5),
#     DestinationCard(Destinations.REGENTS_PARK, Destinations.PICCADILLY_CIRCUS, 5),
#     DestinationCard(Destinations.BAKER_STREET, Destinations.TRAFALGAR_SQUARE, 5),
#     DestinationCard(Destinations.BUCKINGHAM_PALACE, Destinations.ELEPHANT_AND_CASTLE, 5),
#     DestinationCard(Destinations.BIG_BEN, Destinations.TOWER_OF_LONDON, 6),
#     DestinationCard(Destinations.KINGS_CROSS, Destinations.BUCKINGHAM_PALACE, 6),
#     DestinationCard(Destinations.HYDE_PARK, Destinations.ST_PAULS, 6),
#     DestinationCard(Destinations.COVENT_GARDEN, Destinations.TOWER_OF_LONDON, 6),
#     DestinationCard(Destinations.KINGS_CROSS, Destinations.TOWER_OF_LONDON, 7),
#     DestinationCard(Destinations.REGENTS_PARK, Destinations.ELEPHANT_AND_CASTLE, 9),
#     DestinationCard(Destinations.BUCKINGHAM_PALACE, Destinations.BRICK_LANE, 9),
#     DestinationCard(Destinations.BAKER_STREET, Destinations.TOWER_OF_LONDON, 11)
# ]