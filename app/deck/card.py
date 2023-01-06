from enum import Enum
from typing import Optional, Union, List
from .exceptions import SuitError, FaceError, CardValueError


class Suit(Enum):
    DIAMONDS = "DIAMONDS"
    SPADES = "SPADES"
    CLUBS = "CLUBS"
    HEARTS = "HEARTS"


# I'm making the assumption a Jack is a face card for simplicity
class Face(Enum):
    ACE = "ACE"
    JACK = "JACK"
    QUEEN = "QUEEN"
    KING = "KING"


class Card:
    """Represents a card in a deck"""
    suit: Suit
    face_value: Union[Face, int]
    _blackjack_values: List[int]

    def __init__(self, suit: Suit, value: Union[int, Face]):
        """
        Init
        :param suit: Card suit
        :param value: Card value or face (if applicable)
        """
        # Assign values to card
        # Check if suit is valid
        if not isinstance(suit, Suit):
            raise SuitError(f"{suit} is not a valid Suit")
        self.suit = suit

        if isinstance(value, int):
            if (value > 10) or (value < 2):  # Check value face is valid before assigment
                raise ValueError("Invalid value")
            self.face_value = value
        elif isinstance(value, Face):
            self.face_value = value
        else:
            raise CardValueError("Face and Value not valid")

        # Calculate card's black jack value
        if isinstance(self.face_value, int):
            self._blackjack_values = [self.face_value]
        if self.face_value == Face.ACE:
            self._blackjack_values = [1, 11]
        elif self.face_value in [Face.JACK, Face.KING, Face.QUEEN]:
            self._blackjack_values = [10]

    def __int__(self):
        """Returns the high value the card can give in blackjack"""
        return max(self._blackjack_values)

    @property
    def values(self) -> List[int]:
        """
        Card's valid black jack values
        :return:
        """
        return self._blackjack_values

    def __repr__(self):
        return f"{self.suit} | {self.face_value} | {self._blackjack_values}"

    def __eq__(self, other):
        """Allows Equals operator to work"""
        if (self.face_value == other.face_value) and (self.suit == other.suit):
            return True
        else:
            return False

    def __str__(self):
        """Return name of card"""
        return f"{self.face_value} of {self.suit}"

