from deck import Deck
from participant import Participant


class Player(Participant):
    """
    Child class of participant - it deals with anything player related.
    """
    def __init__(self, name: str):
        super().__init__(name)

    def take_turn(self, deck: Deck) -> None:
        """
        checks if player is busted, otherwise lets player hit or stand and prints their current cards and total
        """
        print("-------------------------------")
        print("           Your Turn           ")
        print("-------------------------------")
        while True:
            if self.is_busted():
                return
            user_input = input("hit or stand: ").lower()
            if user_input == "hit": # If player hits a card is added to their cards
                card = deck.deal_card()
                self.take_card(card)
                print(f"You draw: {card}")
                print(f"Your new total: {self.get_total()}")
            elif user_input == "stand": # If player stands their total is printed
                print(f"You stand with: {self.get_total()}")
            else: # In case player doesn't enter hit or stand, they will be reprompted.
                print("Please enter hit or stand")

