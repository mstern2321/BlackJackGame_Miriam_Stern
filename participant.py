from deck import Deck
from hand import Hand
from card import Card
class Participant:
    """
    Parent class for player and dealer
    """
    def __init__(self, name: str) -> None:
        self.name = name
        self.hand = Hand()
    def take_card(self, card: Card) -> None:
        """
        Card is added to the participants hand
        """
        self.hand.add_card(card)

    def show_hand(self) -> str:
        """
        returns cards in participants hand
        """
        return self.hand.show_hand()
    def get_total(self) -> int:
        """
        returns participants total
        """
        return self.hand.get_total()
    def is_busted(self) -> bool:
        """
        Checks if participants total is greater than 21 and returns True
        """
        if self.get_total() > 21:
            return True
        return False
    def take_turn(self, deck: Deck) -> None:
        card = deck.deal_card()
        self.take_card(card)
