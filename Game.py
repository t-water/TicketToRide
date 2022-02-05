from DestinationCards import DestinationCardDeck
from Player import Player

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
    players = [Player() for x in range(num_players)]
    deck = DestinationCardDeck()

    for player in players:
        player.draw_destination_cards(deck)

    for player in players:
        player.confirm_destination_cards(deck)

    for player in players:
        player.print_destination_cards()
    


game()