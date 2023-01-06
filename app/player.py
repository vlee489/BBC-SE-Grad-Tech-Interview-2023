"""
This class represents a player and their hand. Also notes if player is a cpu/AI for use in an end playable
game
"""
from app.hand import Hand


class Player:
    """Represents a player in a game of blackjack"""
    hand: Hand
    cpu: bool

    def __init__(self, cpu: bool = False):
        self.hand = Hand()
        self.cpu = cpu

    def is_bust(self) -> bool:
        """
        If player's hand is bust
        :return: Bool
        """
        return True if (int(self.hand) > 21) else False
