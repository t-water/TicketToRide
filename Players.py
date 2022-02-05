from Player import Player

class Players:
    def __init__(self, numPlayers):        
        self.__players = [Player() for _ in range(numPlayers)]
    
    def __loop_players(self, func, *args):
        for player in self.__players:
            func(player, *args)

    def initialize_transportation_cards(self, transportation_card_deck):
        self.__loop_players(lambda player : player.initialize_transportation_cards(transportation_card_deck))

    def draw_destination_cards(self, destination_card_deck):
        self.__loop_players(lambda player : player.draw_destination_cards(destination_card_deck))

    def confirm_destination_cards(self, destination_card_deck):
        self.__loop_players(lambda player : player.confirm_destination_cards(destination_card_deck))
    
    def print_destination_cards(self):
        self.__loop_players(lambda player : player.print_destination_cards())