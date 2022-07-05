import random
from card import Card


class Deck:
    def __init__(self):
        self.cards = []
        self.create_deck()
        self.shuffle()

    def create_deck(self):
        for s in Card.SUIT_SYMBOLS:
            for v in Card.VALUE_NAMES:
                self.cards.append(Card(s, v))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, num_cards):

        if num_cards > len(self.cards):
            num_cards = len(self.cards)
            print("not enough cards, returning remainder of the deck")
        if num_cards == 1:
            return self.cards.pop()
        return [self.cards.pop() for _ in range(num_cards)]
