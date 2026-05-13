from card import Card
import random
class Deck:
    """
    Represents full deck of cards
    """
    def __init__(self):
       self.cards = []
       self.build_deck()
    def build_deck(self) -> None:
        """
        Builds a deck with 52 cards
        """
        ranks = {"Ace": 11, "Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 10, "Queen": 10, "King": 10}
        suits = ["Club", "Spade", "Heart", "Diamond"]
        for suit in suits: # Creates a card with each suit and rank and appends to list of cards.
            for rank, value in ranks.items():
                card = Card(suit, rank, value)
                self.cards.append(card)
    def shuffle(self) -> None:
        """
        Shuffles the deck of cards
        """
        return random.shuffle(self.cards)
    def deal_card(self) -> Card:
        """
        Removes the last card in deck and returns it
        """
        return self.cards.pop()

    def cards_remaining(self):
        """
        returns the current length of the deck of cards
        """
        return len(self.cards)

deck = Deck()
deck.shuffle()
# print(deck.deal_card())
# print(deck.cards_remaining())
