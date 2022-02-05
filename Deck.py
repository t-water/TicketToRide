import random

starting_deck = {
    "wild": 8,
    "blue": 6,
    "green": 6,
    "black": 6,
    "pink": 6,
    "yellow": 6,
    "orange": 6
}

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