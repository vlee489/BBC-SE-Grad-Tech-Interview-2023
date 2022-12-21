"""Tests for Deck"""
import pytest
from app.deck import Deck, Suit, Card, Face


def test_empty_deck():
    """Tests for empty deck"""
    deck = Deck([])
    assert len(deck) == 0


def test_fresh_deck_size():
    """Tests size of deck with fresh size"""
    deck = Deck.create_fresh_deck()
    assert len(deck) == 52


def test_get_52_random_cards():
    """Test getting 52 random cards actually results in 52 cards"""
    deck = Deck.create_fresh_deck()
    pop_count = 0
    for x in range(52):
        card = deck.get_random_card()
        if isinstance(card, Card):
            pop_count += 1
    assert pop_count == 52


def test_card_list_of_string():
    """Checks if error is throw if cards provided has invalid data type"""
    with pytest.raises(ValueError) as error_info:
        Deck(["this", "is", "Invalid"])


def test_card_list_with_mixed():
    """Tests if error is throw if list with mixed data types are provided"""
    with pytest.raises(ValueError) as error_info:
        cards = ["Invalid", "Card", 1, 4, Card(Suit.HEARTS, value=3), Card(Suit.DIAMONDS, face=Face.KING)]
        Deck(cards)


def test_deck_equals():
    """test if deck are equal"""
    deck_1 = Deck.create_fresh_deck()
    deck_2 = Deck.create_fresh_deck()
    assert deck_1 == deck_2


def test_deck_not_equal():
    """Test that 2 different decks are equal to each other"""
    deck_1 = Deck.create_fresh_deck()
    deck_2 = Deck([])
    assert not deck_1 == deck_2
