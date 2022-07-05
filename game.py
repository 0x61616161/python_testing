from deck import Deck
from hand import Hand


class Game:
    MINIMUM_BET = 1
    START_HAND_SIZE = 2
    WINNING_FACTOR = 2

    def __init__(self, player, dealer):
        self.player = player
        self.dealer = dealer
        self.bet = None
        self.deck = Deck()
        self.play = None

    def start_game(self):
        # Todo: more functions here to make it shorter
        self.dealer.deck = self.deck

        self.play = input(f"You are starting with ${self.player.balance}. Would you like to play a hand? ")

        while self.play.lower() == "yes":
            self.bet = float(input("Place your bet: "))
            if self.bet < Game.MINIMUM_BET:
                print(f"The minimum bet is ${Game.MINIMUM_BET}.")
                continue
            elif self.bet > self.player.balance:
                print("You do not have sufficient funds.")
                continue

            self.player.balance -= self.bet

            self.initialize_hands()

            if self.player.hand.get_value() == 21:
                if self.dealer.hand.get_value() == 21:
                    # tie
                    print("Tie, both blackjack")
                    self.player.balance += self.bet
                else:
                    # player win
                    print(f"Blackjack! You win ${self.bet*1.5} :)")
                    self.player.balance += self.bet*1.5 + self.bet
                continue

            player_points = self.player_play()

            if player_points == 22:
                self.reset()
                self.play = input(f"You are starting with ${self.player.balance}. Would you like to play a hand? ")
                continue

            self.dealer.reveal()
            dealer_points = self.dealer_play()

            print("Dealer points", dealer_points, "Player points", player_points)
            if dealer_points > 21:
                print(f"The dealer busts, you win ${self.bet}:)")
                self.player.balance += self.bet + self.bet
            elif dealer_points == player_points:
                print("You tie. Your bet has been returned.")
                self.player.balance += self.bet
            elif dealer_points > player_points:
                print(f"The dealer wins, you lose ${self.bet} :(")
            else:
                print(f"You win ${self.bet}!")
                self.player.balance += (2 * self.bet)

            self.reset()

    def reset(self):
        self.player.hand = Hand()
        self.dealer.hand = Hand()  # Todo: could also import dealer and just make a completely new dealer here
        self.dealer.deck = Deck()
        self.dealer.flip_card = False
        self.play = input(f"You are starting with ${self.player.balance}. Would you like to play a hand? ")

    def player_play(self):
        current_value = self.player.hand.get_value()
        hit_or_stay = input("Would you like to hit or stay? ")
        while True:
            while not hit_or_stay.lower() in ["hit", "stay"]:
                print("That is not a valid option. ")
                hit_or_stay = input("Would you like to hit or stay? ")
            if hit_or_stay.lower() == "stay":
                return current_value

            c = self.dealer.hit()
            self.player.hand.add_to_hand(c)
            print(f"You are dealt: {c}")
            print(self.player.get_str_hand())
            current_value = self.player.hand.get_value()

            if current_value > 21:
                print(f"Your hand value is over 21 and you lose ${self.bet} :(")
                return 22

            hit_or_stay = input("Would you like to hit or stay? ")

    def dealer_play(self):
        return self.dealer.play()

    def initialize_hands(self):
        for _ in range(Game.START_HAND_SIZE):
            c = self.dealer.hit()  # this should take a param and directly return 2 without need to loop
            self.player.hand.add_to_hand(c)
            c = self.dealer.hit()
            self.dealer.hand.add_to_hand(c)

        print(self.player.get_str_hand())
        print(self.dealer.get_str_hand())