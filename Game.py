from DestinationCards import DestinationCardDeck
from TransportationCards import TransportationCardDeck
from Players import Players

def get_num_players():
    num_players = 0
    min_players = 1
    max_players = 4

    while num_players < min_players or num_players > max_players:
        try:
            get_num_players_message = 'How many people are playing? ({}-{}): '.format(min_players, max_players)
            num_players = int(input(get_num_players_message))
        except ValueError:
            print('Invalid input')
    
    return num_players

def game():
    num_players = get_num_players()
    
    players = Players(num_players)
    destination_card_deck = DestinationCardDeck()
    transportation_card_deck = TransportationCardDeck()

    players.initialize_transportation_cards(transportation_card_deck)
    players.draw_destination_cards(destination_card_deck)
    players.confirm_destination_cards(destination_card_deck)

game()