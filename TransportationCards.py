from collections import Counter, deque
import random
import csv

from TransportationCard import TransportationCard

class TransportationCardDeck:
    def __init__(self):
        self.__cards = deque()
        self.__discard_pile = deque()
        self.__flop = []
        self.__wild = 'wild'
        self.__flop_max_len = 5

        with open('TransportationCards.csv', newline='') as csv_file:
            card_reader = csv.reader(csv_file, delimiter=' ', quotechar='|')

            for row in card_reader:
                entry = row[0].split(',')

                for _ in range(int(int(entry[1]))):
                    self.__cards.append(TransportationCard(entry[0]))
            
        random.shuffle(self.__cards)
        
        self.__maintain_flop()

    def __draw_card(self) -> TransportationCard:
        return self.__cards.popleft()
    
    def draw_cards(self, num_cards) -> list[TransportationCard]:
        return [self.__draw_card() for _ in range(num_cards)]
    
    def initial_deal(self) -> list[TransportationCard]:
        return self.draw_cards(2)

    def __illegal_flop(self) -> bool:        
        return len([card for card in self.__flop if card.is_wild()]) >= 3

    def __maintain_flop(self) -> None:
        if len(self.__cards) == 0:
            self.__cards.extend(self.__discard_pile)
            self.__discard_pile = deque()
            random.shuffle(self.__cards)

        if self.__get_flop_len() < self.__flop_max_len:
            self.__flop.extend(self.draw_cards(self.__flop_max_len - self.__get_flop_len()))
        
        while self.__illegal_flop():
            self.__discard_pile.extend(self.__flop)
            self.__flop.clear()
            self.__flop.extend(self.draw_cards(self.__flop_max_len))
            
    
    def can_take_turn(self) -> bool:
        return self.__get_flop_len() > 0
    
    def __take_from_flop(self, index) -> TransportationCard:
        selected_card = self.__flop.pop(index)

        self.__maintain_flop()

        return selected_card

    def __get_user_choice(self) -> TransportationCard:
        flop_len = self.__get_flop_len()

        for i in range(flop_len):
            print(str(i) + ': ' + str(self.__flop[i]))
        
        print(str(flop_len) + ': Blind Draw')

        user_choice = int(input())

        if 0 <= user_choice < flop_len:
            return self.__take_from_flop(user_choice)
        else:
            return self.__draw_card()

    def take_turn(self) -> list[TransportationCard]:
        cards_taken = []

        first_card_taken = self.__get_user_choice()
        cards_taken.append(first_card_taken)

        if first_card_taken != self.__wild:
            cards_taken.append(self.__get_user_choice())

        return cards_taken
    
    def __get_flop_len(self) -> int:
        return len(self.__flop)