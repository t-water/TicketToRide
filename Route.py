class Route:
    def __init__(self, v1, v2, color, length):
        self.__v1 = v1
        self.__v2 = v2
        self.__color = color
        self.__length = length
        self.__taken_by = None
    
    def __str__(self):
        return self.__v1 + ' -> ' + self.__v2 + ' (' + self.__color + ') = ' + str(self.__length)
    
    def is_claimed(self):
        return self.__taken_by != None
    
    def can_claim(self, transportation_cards) -> bool:
        if self.is_claimed():
            return False
        
        c = {}

        for card in transportation_cards:
            key = str(card)

            c.setdefault(key, 0)
            c[key] += 1
        
        if self.__is_wild():
            for key in c.keys():
                if key != 'wild' and c[key] + c['wild'] >= self.__length:
                    return True

            return False
        else:
            return c[self.__color] >= self.__length
        
    def __is_wild(self):
        return self.__color == 'wild'

    def get_score(self):
        return self.__length * (self.__length - 1) / 2 + 1
