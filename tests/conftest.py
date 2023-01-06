"""Pytest Configuration"""
from app.game import Game
from typing import Union
import pytest


class SharedStorage:
    game: Union[Game, None]

    def __init__(self):
        game = None


def pytest_configure():
    pytest.shared = SharedStorage()
