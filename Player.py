class Player:
    def __init__(self, destination_card_deck, transportation_card_deck):
        self.__destination_card_deck = destination_card_deck
        self.__transportation_card_deck= transportation_card_deck
        self.__player_destination_cards = []
        self.__player_transportation_cards = []
        self.__points = 0
        self.__num_busses = 16
    
    def draw_destination_cards(self):
        self.__player_destination_cards = self.__destination_card_deck.draw()

    def confirm_destination_cards(self):
        card_len = len(self.__player_destination_cards)

        for i in range(card_len):
            print (str(i) + ': give back ' + str(self.__player_destination_cards[i]))
        
        print(str(card_len) + ': keep all cards')

        card_to_return = -1

        while card_to_return < 0:
            try:
                card_to_return = int(input())
            except ValueError:
                print('Invalid value')

        if card_to_return < card_len:
            self.__destination_card_deck.return_card(self.__player_destination_cards.pop(card_to_return))

    def print_destination_cards(self):
        if len(self.__player_destination_cards) == 0:
            print ('No destination cards currently')
        else:
            for card in self.__player_destination_cards:
                print(card)
    
    def initialize_transportation_cards(self):
        self.__player_transportation_cards.extend(self.__transportation_card_deck.initial_deal())
    
    def print_transportation_cards(self):
        print(self.__player_transportation_cards)
    
    def get_num_busses(self):
        return self.__num_busses
    
    def take_turn(self):
        if self.__transportation_card_deck.can_take_turn():
            print('0: Take a transportation card')
        
        user_choice = int(input())

        transportation_cards_obtained = self.__transportation_card_deck.take_turn()
        self.__player_transportation_cards.extend(transportation_cards_obtained)