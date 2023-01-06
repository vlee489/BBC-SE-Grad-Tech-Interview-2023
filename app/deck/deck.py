from .card import Card, Suit, Face
from typing import List, Optional
import random


class Deck:
    """Represents a Deck of cards"""
    cards: List[Card]
    _removed_cards: List[Card]

    def __init__(self, cards: List[Card]):
        """
        Init
        :param cards: cards to place into deck
        """
        # Check if list only of cards only contains Card
        if len(cards):
            valid = True
            for card in cards:
                if not isinstance(card, Card):
                    valid = False
            if not valid:
                raise ValueError("Cards contain non Card objects")
        # Assign cards to object
        self.cards = cards
        self._removed_cards = []

    def __len__(self):
        """Return length of card array of Deck"""
        return len(self.cards)

    def get_random_card(self) -> Optional[Card]:
        """
        Get a random card from the deck
        :return: Card or None
        """
        if self.cards:
            choice = random.randint(0, self.__len__() - 1)
            pop = self.cards.pop(choice)
            self._removed_cards.append(pop)
            return pop

    @classmethod
    def create_fresh_deck(cls):
        """Creates a fresh deck of cards"""
        cards = []
        for suit in Suit:
            for val in range(2, 11):
                cards.append(Card(suit, val))
            for face in Face:
                cards.append(Card(suit, face))
        return cls(cards)

    def __eq__(self, other):
        match_count = 0  # Hold number of matching cards
        for x in self.cards:  # For each card in ourselves
            # Iterate and find if card matches
            for y in range(len(other.cards)):
                if other.cards[y] == x:
                    # If matches increment matching card counter
                    match_count += 1
        # if the match count is the same length of the cards we're testing in both we can return True
        if (match_count == len(self)) and (match_count == len(other)):
            return True
        return False

    def __iter__(self):
        self.__iter_card = 0
        return self

    def __next__(self):
        if self.__iter_card < self.__len__():
            card = self.cards[self.__iter_card]
            self.__iter_card += 1
            return card
        else:
            raise StopIteration






