from typing import List, Optional, Dict
from app.player import Player
from app.deck import Card, Deck


class Game:
    """Represents a game of Blackjack"""
    players: Dict[int, Player]
    deck: Deck

    def __init__(self, deck: Deck, players: Dict[int, Player]):
        """
        Init
        :param deck: card deck
        :param players: players
        """
        self.players = players
        self.deck = deck

    @classmethod
    def create_game(cls, players_count: int, cpu_count: int):
        """
        Create new game of Blackjack
        :param players_count: number of players
        :param cpu_count: number of CPUs
        :return: Game
        """
        players = {}
        for p in range(players_count):
            players[(len(players) + 1)] = Player()
        for c in range(cpu_count):
            players[(len(players) + 1)] = Player(cpu=True)
        return cls(Deck.create_fresh_deck(), players)

    def initial_hand(self) -> None:
        """
        Give out initial hand to players and dealer
        :return: None
        """
        for x in range(2):
            for player in self.players.values():
                player.hand.add_card(self.deck.get_random_card())

    def hit(self, player: int) -> Optional[Card]:
        """
        Draw a card for a player
        :param player: player number
        :return: card drawn
        """
        card = self.deck.get_random_card()
        if card:  # If card is not None
            self.players[player].hand.add_card(card)
        return card
