#to do:
# make a function that picks a random card that is created in the cards file.

import random
import cards



def main():
    deck = cards.deck()
    drawn_cards= []
    for _ in range(3):
        drawn_card = deck.draw_card()
        if drawn_card:
            print(f"you drew, {drawn_card}")
            drawn_cards.append(str(cards))
        else:
            print("the deck is empty")
main()