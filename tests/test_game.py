"""Tests for Deck"""
import pytest
from app.deck import Deck, Suit, Card, Face
from app.game import Game


def test_initial_hand():
    """Test that 2 cards per player are given initially"""
    game = Game.create_game(4, 1)  # 5 players total
    game.initial_hand()
    is_correct = True
    for player in game.players.values():
        if len(player.hand) != 2:
            is_correct = False
    assert is_correct
