"""Tests for Hand"""
import pytest
from app.hand import Hand
from app.deck import Card, Deck, Suit, Face


def test_creating_hand_len():
    """Test creating a blank hand"""
    hand = Hand()
    assert len(hand) == 0


def test_total_card_bj_value():
    """Test total of hand is 380"""
    # We're doing 380 as the total as that's the highest value you can get with all cards added together
    hand = Hand()
    deck = Deck.create_fresh_deck()
    for x in range(len(deck)):
        hand.add_card(deck.get_random_card())
    assert int(hand) == 380


def test_single_ace_cal():
    """Tests calculating score for one ace card"""
    hand = Hand()
    hand.add_card(Card(suit=Suit.HEARTS, face=Face.ACE))
    assert int(hand) == 11


def test_two_ace_cal():
    """Tests calculating score for two ace card"""
    hand = Hand()
    hand.add_card(Card(suit=Suit.HEARTS, face=Face.ACE))
    hand.add_card(Card(suit=Suit.SPADES, face=Face.ACE))
    assert int(hand) == 12


def test_value_1():
    """First test of adding values"""
    hand = Hand()
    hand.add_card(Card(suit=Suit.HEARTS, face=Face.ACE))  # 1
    hand.add_card(Card(suit=Suit.SPADES, face=Face.ACE))  # 1
    hand.add_card(Card(suit=Suit.DIAMONDS, face=Face.KING))  # 10
    assert int(hand) == 12


def test_value_2():
    """Second test of adding values"""
    hand = Hand()
    hand.add_card(Card(suit=Suit.CLUBS, face=Face.ACE))  # 1
    hand.add_card(Card(suit=Suit.SPADES, face=Face.KING))  # 10
    hand.add_card(Card(suit=Suit.HEARTS, face=Face.KING))  # 10
    assert int(hand) == 21


def test_value_3():
    """Third test of adding values"""
    hand = Hand()
    hand.add_card(Card(suit=Suit.DIAMONDS, face=Face.ACE))  # 11
    hand.add_card(Card(suit=Suit.HEARTS, face=Face.ACE))  # 11
    hand.add_card(Card(suit=Suit.SPADES, face=Face.KING))  # 10
    hand.add_card(Card(suit=Suit.CLUBS, face=Face.KING))  # 10
    assert int(hand) == 42


def test_all_value_1():
    """Test returning of all valid values from hand for single ace"""
    hand = Hand()
    hand.add_card(Card(suit=Suit.DIAMONDS, face=Face.ACE))
    assert set().union(*[hand.values(), [1, 11]])


def test_all_value_2():
    """Test returning of all valid values from hand for a full deck"""
    hand = Hand()
    deck = Deck.create_fresh_deck()
    for x in range(len(deck)):
        hand.add_card(deck.get_random_card())
    assert set().union(*[hand.values(), [350, 360, 370, 380]])


def test_get_item():
    """Test get item"""
    hand = Hand()
    hand.add_card(Card(suit=Suit.DIAMONDS, face=Face.ACE))
    card = Card(suit=Suit.HEARTS, face=Face.ACE)
    hand.add_card(card)  # index 1
    hand.add_card(Card(suit=Suit.SPADES, face=Face.KING))
    hand.add_card(Card(suit=Suit.CLUBS, face=Face.KING))
    assert hand[1] == card
