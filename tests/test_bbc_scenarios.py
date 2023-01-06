"""Tests for Scenarios in BBC interview doc"""
import pytest
from app.hand import Hand
from app.deck import Card, Deck, Suit, Face
from app.game import Game


def test_scenario_one():
    """Test that 2 cards for the single player"""
    game = Game.create_game(1, 0)  # 1 player
    pytest.shared.game = game  # Store hand in Pytest's local test memory for recall later
    game.initial_hand()
    # The game will always start players from 1
    player_hand = game[1].hand
    assert len(player_hand) == 2


def test_scenario_two():
    """if hand is valid take another card"""
    game = pytest.shared.game
    player_hand: Hand = game[1].hand
    if player_hand.valid():
        initial_score = int(player_hand)
        game.hit(1)
        assert initial_score != int(player_hand)
    else:
        pytest.skip(f"Skipped Test: Hand not valid {player_hand.values()}")


# We don't test scenario three (if stand) due having no stand function due to my implementation of game

def test_scenario_four_and_five():
    """if hand is valid and score of 21"""
    game = pytest.shared.game
    player_hand: Hand = game[1].hand
    if int(player_hand) <= 21:
        assert player_hand.valid()
    elif int(player_hand) > 21:
        assert not player_hand.valid()


def test_scenario_six():
    """Test value when hand has a king and ace"""
    hand = Hand()
    hand.add_card(Card(Suit.DIAMONDS, Face.KING))  # 10
    hand.add_card(Card(Suit.HEARTS, Face.ACE))  # 11
    assert int(hand) == 21


def test_scenario_seven():
    """Test value when hand has a king, queen and ace"""
    hand = Hand()
    hand.add_card(Card(Suit.DIAMONDS, Face.KING))  # 10
    hand.add_card(Card(Suit.DIAMONDS, Face.QUEEN))  # 10
    hand.add_card(Card(Suit.HEARTS, Face.ACE))  # 1
    assert int(hand) == 21


def test_scenario_eight():
    """Test value when hand has a king, queen and ace"""
    hand = Hand()
    hand.add_card(Card(Suit.DIAMONDS, 9))  # 10
    hand.add_card(Card(Suit.DIAMONDS, Face.ACE))  # 10
    hand.add_card(Card(Suit.HEARTS, Face.ACE))  # 1
    assert int(hand) == 21
