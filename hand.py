import random

from card import Card
from deck import Deck
class Hand:
    """
    Represents the cards held by one participant
    """
    def __init__(self):
        self.cards = []
    def add_card(self, card: Card) -> None:
        """
        Adds cards to participants cards
        """
        self.cards.append(card)
    def get_total(self) -> int:
        """
        Returns participants total
        """
        total = 0
        aces = 0
        for card in self.cards:
            if card.rank == "Ace":
                aces += 1
            total += card.value
        while total > 21 and aces > 0: # while the participants total is greater than 21 and there are aces in the participant's cards

                total -= 10 # Take away 10 so that the ace is only worth one
                aces -= 1
        return total

    def show_hand(self) -> str:
        """
        Returns the cards in the participants hands as a formatted string
        """
        formatted = []
        for card in self.cards:
            formatted.append(str(card)) # Turn card into string so it's not just a card object
        return ", ".join(formatted) # Puts all cards into a list separated by commas


    def __str__(self):
        return f"Players cards: {self.show_hand()} \nPlayers total: {self.get_total()}"


hand = Hand()
deck = Deck()
deck.shuffle()
hand.add_card(deck.deal_card())
hand.add_card(deck.deal_card())
hand.add_card(deck.deal_card())
hand.add_card(deck.deal_card())
hand.add_card(deck.deal_card())



# print(hand)
