from participant import Participant


class Player(Participant):
    def __init__(self, balance):
        super().__init__()
        self.balance = balance

    def get_str_hand(self):
        result = "Player's hand: "
        for card in self.hand.cards:
            result += f"{card}, "

        if len(result) > 2:
            return result[:-2]

        result += f"Player's hand value is {self.hand.get_value()}"

        return result
