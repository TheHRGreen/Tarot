#defining suits
suits = ("Swords", "Cups", "Wands," "Pentacles")

# defining minor arcana

class Minor_Arcana_Card:
    def __init__(self, suit, number):
        if number not in range (1, 14):
            raise Exception("number must be between 1 and 14")
        if suit not in suits:
            raise Exception("suit must be 'Swords', 'Cups', 'Wands', 'Pentacles'")
        self.suit
        self.number
    