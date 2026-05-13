
from deck import Deck
from participant import Participant

class Dealer(Participant):
    """
    Child class of participant - it takes care of anything dealer related.
    """
    def __init__(self, name):
        super().__init__(name)
    def show_first_card(self) -> str:
        """
        returns the dealers first card
        """
        return str(self.hand.cards[0])
    def take_turn(self, deck: Deck) -> None:
        """
        As long as the dealer's total is less than 17, a card is added to the dealers cards.
        """
        while self.get_total() < 17:
            card = deck.deal_card()
            self.take_card(card)
            print(f"Dealer takes: {card}")
            print(f"Dealer current total: {self.get_total()}")
deck = Deck()
dealer = Dealer("Miriam")


# print(dealer.show_first_card())