#need to do:
# assign each minor arcana class containing both the cards number and suit
# If the number should instead be a face card change it so it prints the face card instead of the number when the card is drawn


#defining suits
import random


# defining minor arcana

class Minor_Arcana_Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return f"{self.rank} of {self.suit}"

class deck:
    def __init__(self):
        self.cards = []
        self.populate()
        self.drawn_cards = []

    def populate(self):
        suits = ["Cups", "Pentacles", "Swords","Wands"]
        ranks = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Page", "Knight", "Queen", "King"]
        for suit in suits:
            for rank in ranks:
                self.cards.append(Minor_Arcana_Card(suit,rank))

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        if len(self.cards) == 0:
            return None
        card = random.choice(self.cards)
        self.cards.remove(card)
        self.drawn_cards.append(card)
        return card
    

    

