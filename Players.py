from Player import Player

class Players:
    def __init__(self, numPlayers, destination_card_deck, transportation_card_deck):        
        self.__players = [Player(destination_card_deck, transportation_card_deck) for _ in range(numPlayers)]
        self.__turns = 0
    
    def __loop_players(self, func, *args):
        for player in self.__players:
            func(player, *args)

    def initialize_transportation_cards(self):
        self.__loop_players(lambda player : player.initialize_transportation_cards())

    def draw_destination_cards(self):
        self.__loop_players(lambda player : player.draw_destination_cards())

    def confirm_destination_cards(self):
        self.__loop_players(lambda player : player.confirm_destination_cards())
    
    def print_destination_cards(self):
        self.__loop_players(lambda player : player.print_destination_cards())
    
    def __increment_turn(self):
        self.__turns += 1
    
    def take_turns(self):
        num_players = len(self.__players)
        current_turn = self.__turns % num_players
        current_player = self.__players[current_turn]

        while current_player.get_num_busses() > 2:
            print('Player ' + str(current_turn + 1) + "'s Turn")
            current_player.take_turn()
            self.__increment_turn()
            current_turn = self.__turns % num_players
            current_player = self.__players[current_turn]