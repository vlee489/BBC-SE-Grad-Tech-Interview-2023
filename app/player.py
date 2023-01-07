"""
This class represents a player and their hand. Also notes if player is a cpu/AI for use in an end playable
game
"""
from app.hand import Hand


class Player:
    """Represents a player in a game of blackjack"""
    hand: Hand
    cpu: bool
    text_colour: str
    show_bust: bool
    player_num: int

    def __init__(self, player_num: int, text_colour: str, cpu: bool = False):
        self.hand = Hand()
        self.player_num = player_num
        self.cpu = cpu
        self.text_colour = text_colour
        self.show_bust = False

    def is_bust(self) -> bool:
        """
        If player's hand is bust
        :return: Bool
        """
        return True if (int(self.hand) > 21) else False
