from hand import Hand


class Participant:
    def __init__(self):
        self._hand = Hand()

    @property
    def hand(self):
        return self._hand

    @hand.setter
    def hand(self, hand):
        self._hand = hand

    def get_str_hand(self):
        raise NotImplementedError
