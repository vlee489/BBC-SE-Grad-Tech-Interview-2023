"""Tests for Deck"""
import pytest
from app.deck import Suit, Card, Face, CardValueError, FaceError, SuitError


def test_invalid_suit():
    """Test creating card with invalid suit"""
    with pytest.raises(SuitError) as error_info:
        Card("Invalid Suit", 3)


def test_invalid_face():
    """Test creating card with invalid face"""
    with pytest.raises(CardValueError) as error_info:
        Card(Suit.SPADES, "invalid face")


def test_value_too_low():
    """Test when value is too low"""
    with pytest.raises(ValueError) as error_info:
        Card(Suit.DIAMONDS, 1)


def test_value_too_high():
    """Test when value is too high"""
    with pytest.raises(ValueError) as error_info:
        Card(Suit.DIAMONDS, 11)


def test_invalid_value_type():
    """Test when value is not an int"""
    with pytest.raises(CardValueError) as error_info:
        Card(Suit.DIAMONDS, "11")


def test_card_value_equal():
    """Test 2 card object with same value and suit are equal"""
    card_1 = Card(Suit.HEARTS, 10)
    card_2 = Card(Suit.HEARTS, 10)
    assert card_1 == card_2


def test_card_face_equal():
    """Test 2 card object with same face and suit are equal"""
    card_1 = Card(Suit.HEARTS, Face.KING)
    card_2 = Card(Suit.HEARTS, Face.KING)
    assert card_1 == card_2


def test_card_not_equal_face_or_value():
    """Test 2 card object with different info are not equal"""
    card_1 = Card(Suit.HEARTS, 10)
    card_2 = Card(Suit.HEARTS, Face.KING)
    assert not (card_1 == card_2)


def test_card_face_not_equal():
    """Test 2 card object with different face aren't equal"""
    card_1 = Card(Suit.SPADES, Face.KING)
    card_2 = Card(Suit.HEARTS, Face.KING)
    assert not (card_1 == card_2)


def test_card_value_and_suit_not_equal():
    """Test 2 card object with different face aren't equal"""
    card_1 = Card(Suit.SPADES, 2)
    card_2 = Card(Suit.HEARTS, 10)
    assert not (card_1 == card_2)
