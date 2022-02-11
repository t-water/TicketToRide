class TransportationCard:
    def __init__(self, val):
        self.__val = val
    
    def get_val(self):
        return self.__val

    def __str__(self):
        return self.get_val()
    
    def is_wild(self):
        return self.__val == 'wild'