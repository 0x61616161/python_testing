from participant import Participant


class Dealer(Participant):
    def __init__(self):
        super().__init__()
        self.flip_card = False
        self.deck = None

    def hit(self):
        c = self.deck.deal(1)
        return c

    def reveal(self):
        self.flip_card = True
        print("Revealing: ", self.get_str_hand())

    def get_str_hand(self):
        result = "Dealer's hand: "
        if self.flip_card:
            for card in self.hand.cards:
                result += f"{card}, "
        else:
            return f"Dealer's hand: {self.hand.cards[0]}, Unknown"
        if len(result) > 2:
            return result[:-2]
        return result

    # Todo: This should probably be part of game class, otherwise players should have the play also in player, but that introduces a lot of dependencies
    def play(self):
        while True:
            value = self.hand.get_value()
            if value > 17:
                return value
            c = self.hit()
            self.hand.add_to_hand(c)
            print(f"Dealer got {c}")
            print(self.get_str_hand())
