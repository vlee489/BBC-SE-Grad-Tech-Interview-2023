from typing import List, Optional
from app.deck import Card, Face


class Hand:
    """Represents a player's hand"""
    cards: List[Card]  # cards in a player's hand

    def __init__(self):
        """Init"""
        self.cards = []

    def add_card(self, card: Card) -> None:
        """
        Add a card to a player's hand
        :param card: Card to add to hand
        :return: None
        """
        self.cards.append(card)

    def values(self) -> List[int]:
        """
        Returns a list of valid values of the hand
        :return: valid values for hand
        """
        value = 0
        ace_cards = 0  # counter for number of aces in hand
        for card in self.cards:
            value += int(card)
            if card.face_value == Face.ACE:  # Keep count of number of ace cards
                ace_cards += 1
        # Work out all the possible values with aces and return
        return [value - (aces_as_1 * 10) for aces_as_1 in range(ace_cards + 1)]

    def __int__(self) -> int:
        """passes closest value to 21"""
        values = self.values()  # Get list of values
        if len(values) == 1:
            # if the list of value when ace is present has no values, return first value
            return values[0]
        elif len(values) > 1:
            for x in values:  # iterate through list
                if x <= 21:
                    # if value = or less than 21, return the value
                    return x
            # If we hit the end of the list with no return, then we return the highest value, which is index 0
            return values[0]
        return 0  # if we have no values, return 0

    def __len__(self) -> int:
        """return number of cards in hand"""
        return len(self.cards)

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

    def __getitem__(self, item):
        return self.cards[item]
