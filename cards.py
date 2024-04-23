#need to do:
# assign each minor arcana class containing both the cards number and suit
# If the number should instead be a face card change it so it prints the face card instead of the number when the card is drawn


#defining suits
import random


# defining minor arcana

class TarotCard:
    def __init__(self, suit=None, rank=None, name=None, number=None):
        self.suit = suit
        self.rank = rank
        self.name = name
        self.number = number


    def __str__(self):
        if self.suit and self.rank:
            return f"{self.rank} of {self.suit}" #minor arcana
        elif self.name and self.number is not None:
            return f"{self.number}: {self.name}:" #major arcana


class deck:
    def __init__(self):
        self.cards = []
        self.populate()
        self.shuffle()
        #self.drawn_cards = []



    def populate(self):
        major_arcana_names = ["The Fool", "The Magician", "The High Priestess", "The Empress", "The Emperor",
            "The Hierophant", "The Lovers", "The Chariot", "Strength", "The Hermit",
            "Wheel of Fortune", "Justice", "The Hanged Man", "Death", "Temperance",
            "The Devil", "The Tower", "The Star", "The Moon", "The Sun",
            "Judgement", "The World"
        ]

        for i, name in enumerate(major_arcana_names):
            self.cards.append(TarotCard(name=name, number=i))


        suits = ["Cups", "Pentacles", "Swords","Wands"]
        ranks = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Page", "Knight", "Queen", "King"]
        for suit in suits:
            for rank in ranks:
                self.cards.append(TarotCard(suit=suit, rank=rank))


    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        if len(self.cards) == 0:
            return None
        else:
            return self.cards.pop()






        ##card = random.choice(self.cards)
        ##self.cards.remove(card)
        ##self.drawn_cards.append(card)
        ##return card
    

    

