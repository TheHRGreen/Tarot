#to do:
# make a function that picks a random card that is created in the cards file.

import random
import cards

def main():
    deck = cards.deck()
    deck.shuffle()
    drawn_card = deck.draw_card()
    if drawn_card:
        print("you drew", drawn_card)
    else:
        print("the deck is empty")
main()