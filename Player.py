class Player:
    def __init__(self):
        self.__destination_cards = []
    
    def draw_destination_cards(self, deck):
        self.__destination_cards = deck.draw()

    def confirm_destination_cards(self, deck):
        card_len = len(self.__destination_cards)

        for i in range(card_len):
            print (str(i) + ': give back ' + str(self.__destination_cards[i]))
        
        print(str(card_len) + ': keep all cards')

        card_to_return = -1

        while card_to_return < 0:
            try:
                card_to_return = int(input())
            except ValueError:
                print('Invalid value')

        if card_to_return < card_len:
            deck.return_card(self.__destination_cards.pop(card_to_return))

    def print_destination_cards(self):
        if len(self.__destination_cards) == 0:
            print ('No destination cards currently')
        else:
            for card in self.__destination_cards:
                print(card)