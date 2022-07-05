class Hand:
    def __init__(self):
        self._cards = []

    @property
    def cards(self):
        return self._cards

    @cards.setter
    def cards(self, value):
        self._cards = value

    def get_value(self):
        # Todo: The calculation here is very bad, can surely be improved
        value = 0
        num_aces = 0
        for c in self.cards:
            if c.value != 1:
                if c.value > 10:
                    value += 10
                else:
                    value += c.value
            else:
                num_aces += 1

        if num_aces == 0:
            return value
        num_ones = num_aces

        # testing with different number of ace values  (1 and 11)
        # start by testing all aces with value of 1 and changing to value of 11 (one ace at a time)
        while True:
            temp_value = value
            temp_aces = num_aces - num_ones
            for i in range(num_aces):
                if i < temp_aces:
                    temp_value += 11
                else:
                    temp_value += 1
            if temp_value > 21 and num_ones == num_aces:
                return temp_value
            elif temp_value > 21 and num_ones < num_aces:
                temp_value -= 10
                return temp_value
            else:  # change one ace value from 1 to 11
                if num_ones == 0:
                    return temp_value
                for i in range(num_ones):
                    temp_value -= 1
                num_ones -= 1
                if num_ones < 0:  # ideally this should not happen
                    print("num ones smaller 0 ", num_ones)
                    break

        return value

    def add_to_hand(self, card):
        self.cards.append(card)

    def __str__(self):
        return f"Current hand, {self.cards}"
