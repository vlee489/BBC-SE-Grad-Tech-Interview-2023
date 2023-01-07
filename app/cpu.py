"""Functions used for CPU to make decision in a game"""
import random
from app.hand import Hand


def cpu_decision(hand: Hand, deck_size: int):
    """
    Decides if the cpu should hit or stand
    :param hand: CPU's hand
    :param deck_size: the size of the deck remaining
    :return: bool, True = Hit, False = Stand
    """
    # TODO : add actual logic
    return bool(random.getrandbits(1))

