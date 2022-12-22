from typing import List
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

    def closest_value(self) -> int:
        """
        Returns the hand's value closest to 21
        :return: int
        """
        value = 0
        ace_cards = 0  # counter for number of aces in hand
        for card in self.cards:
            # If card
            if len(card.values) == 1:
                value += int(card)
            elif card.face_value == Face.ACE:
                ace_cards += 1
        possible_values_with_ace: List[int] = []
        # Calculate mix of value for number of we have ace cards
        for a in range(ace_cards):
            if not possible_values_with_ace:  # If no card in array yet, we add the initial values
                possible_values_with_ace += [(value + 11), (value + 1)]
            else:  # If the array has values
                new_possible_value: List[int] = []  # Temp array to avoid editing array we're iterating through
                for pv in possible_values_with_ace:
                    new_possible_value += [(pv + 11), (pv + 1)]
                possible_values_with_ace = new_possible_value

        # Work out best return value
        if not possible_values_with_ace:
            # if the list of value when ace is present has no values, return main value
            return value
        else:
            possible_values_with_ace.sort(reverse=True)  # Sort value high to low
            for x in possible_values_with_ace:  # iterate through list
                if x <= 21:
                    # if value = or less than 21, return the value
                    return x
            # If we hit the end of the list with no return, then we return the highest value
            return possible_values_with_ace[0]

    def __int__(self) -> int:
        """passes closest value"""
        return self.closest_value()

    def __len__(self) -> int:
        """return number of cards in hand"""
        return len(self.cards)

    def __iter__(self):
        self.iter_card = 0
        return self

    def __next__(self):
        if self.iter_card < self.__len__():
            card = self.cards[self.iter_card]
            self.iter_card += 1
            return card
        else:
            raise StopIteration
