"""List of exceptions for deck and cards"""


class SuitError(Exception):
    """Invalid Suit"""
    pass


class FaceError(Exception):
    """Invalid Face"""
    pass


class CardValueError(Exception):
    """no card value or face provided"""
    pass
