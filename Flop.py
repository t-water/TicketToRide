from collections import Counter

class Flop:
    def __init__(self):
        self.__flop = []
        self.__wild = 'wild'
    
    def initialize_flop(self, card_source, card_dump):
        pass

    def flop(self):
        while len(self.__flop) == 0 or self.__illegal_flop():
            self.__discard_pile.extend(self.__flop)
            self.__flop.clear()
            self.__flop.extend(self.draw_cards(5))

    def __illegal_flop(self):
        c = Counter(self.__flop)
        
        return c[self.__wild] >= 3
    
    def take_turn(self):
        flop_len = len(self.__flop)
        cards_taken = []

        for i in range(flop_len):
            print(str(i) + ': ' + self.__flop[i])
        
        print(str(flop_len) + ': Blind Draw')

        user_choice = int(input())

        if 0 <= user_choice < flop_len:
            cards_taken.append(self.__flop.pop(user_choice))
        
        return cards_taken
        
