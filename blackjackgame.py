
from deck import Deck
from player import Player
from dealer import Dealer

class BlackJackGame:
    """
    Controller class for blackjack game
    """
    def __init__(self, player_name: str):
        self.deck = Deck()
        self.deck.shuffle()
        self.player = Player(player_name)
        self.dealer = Dealer("dealer")
        self.player_name = player_name

    def initial_deal(self):
        """
        Gives 2 cards to player and dealer.
        """
        for _ in range(2):
            self.dealer.take_card(self.deck.deal_card())
            self.player.take_card(self.deck.deal_card())
    def show_game_state(self):
        """
        Prints game state before determining winner
        """
        print("-------------------------------")
        print("          Final Hands          ")
        print("-------------------------------")
        print(f"Dealer hand: {self.dealer.show_hand()}")
        print(f"Dealer total: {self.dealer.get_total()}")
        print()
        print(f"Player hand: {self.player.show_hand()}")
        print(f"Player total: {self.player.get_total()}")

    def determine_winner(self):
        """
        Determines winner
        """

        if self.player.get_total() > 21: # If the player's total is greater than 21, the dealer wins.
            return self.dealer.name

        elif self.dealer.get_total() > 21: # If the dealer's total is greater than 21, the player wins.
            return self.player.name
        else:
            if self.player.get_total() == self.dealer.get_total(): # If player and dealer have the same total, there is a tie.
                return f"It's a tie!"
            elif self.player.get_total() > self.dealer.get_total(): # If player and total both don't have 21, the one with more points wins.
                return self.player.name
            return self.dealer.name # Returns winners name or it's a tie
    def play(self):
        """
        Runs the game
        """

        self.initial_deal()

        self.player.take_turn(self.deck)

        if not self.player.is_busted():
            self.dealer.take_turn(self.deck)

        self.show_game_state()
        print("-------------------------------")
        print("             Result            ")
        print("-------------------------------")
        winner = self.determine_winner()
        if winner == "!t's a tie!":
            print(winner)
        else:
            print(f"{winner} won!")


print("Welcome to Blackjack!")
user_name = input("Enter your name: ")

game = BlackJackGame(user_name)
game.play()

