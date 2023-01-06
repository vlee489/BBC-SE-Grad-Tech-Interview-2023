"""Tests for Scenarios in BBC interview doc"""
import pytest
from app.hand import Hand
from app.deck import Card, Deck, Suit, Face


def test_given_king_and_ace():
    """Test value when hand has a king and ace"""
    hand = Hand()
    hand.add_card(Card(Suit.DIAMONDS, Face.KING))  # 10
    hand.add_card(Card(Suit.HEARTS, Face.ACE))  # 11
    assert int(hand) == 21


def test_given_king_queen_and_ace():
    """Test value when hand has a king, queen and ace"""
    hand = Hand()
    hand.add_card(Card(Suit.DIAMONDS, Face.KING))  # 10
    hand.add_card(Card(Suit.DIAMONDS, Face.QUEEN))  # 10
    hand.add_card(Card(Suit.HEARTS, Face.ACE))  # 1
    assert int(hand) == 21


def test_given_nine_ace_and_ace():
    """Test value when hand has a king, queen and ace"""
    hand = Hand()
    hand.add_card(Card(Suit.DIAMONDS, 9))  # 10
    hand.add_card(Card(Suit.DIAMONDS, Face.ACE))  # 10
    hand.add_card(Card(Suit.HEARTS, Face.ACE))  # 1
    assert int(hand) == 21