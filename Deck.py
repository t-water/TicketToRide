import random
import csv

starting_deck = { }

with open('TransportationCards.csv', newline='') as csv_file:
    card_reader = csv.reader(csv_file, delimiter=' ', quotechar='|')
    for row in card_reader:
        entries = row[0].split(',')
        starting_deck[entries[0]] = int(entries[1])

def draw_card():
    deck_cards = [key for key in starting_deck.keys() if starting_deck[key] > 0]

    if len(deck_cards) > 0:
        card = random.choice(deck_cards)
        starting_deck[card] = starting_deck[card] - 1
        
        return card
    else:
        return None

def process_deck():
    drawn_card = draw_card()

    while drawn_card:
        print (drawn_card, starting_deck[drawn_card])

        drawn_card = draw_card()

process_deck()