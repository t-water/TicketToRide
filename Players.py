from Player import Player
import random

class Players:
    def __init__(self, numPlayers):        
        self.__players = [Player() for _ in range(numPlayers)]
        self.__turns = 0
    
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
    
    def __increment_turn(self):
        self.__turns += 1
    
    def take_turns(self):
        num_players = len(self.__players)
        current_turn = self.__turns % num_players
        current_player = self.__players[current_turn]

        while current_player.get_num_busses() > 2:
            print ('player ' + str(current_turn) + ' has ' + str(current_player.get_num_busses()) + ' buses')
            current_player.use_busses(random.randint(1, 4))
            
            self.__increment_turn()
            current_turn = self.__turns % num_players
            current_player = self.__players[current_turn]