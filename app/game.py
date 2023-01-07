"""
This Game class acts as a place to store a deck of cards and the hands of players
it has no logic for working playing the game, that's determined by the player(what uses this class)
"""
from typing import List, Optional, Dict
from app.player import Player
from app.deck import Card, Deck
import copy


# Used to colour terminal output
term_colours = ["red", "green", "yellow", "blue", "magenta", "cyan"]


class Game:
    """Represents a game of Blackjack"""
    players: List[Player]
    deck: Deck

    def __init__(self, deck: Deck, players: List[Player]):
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
        player_count = 1
        players = []
        # We use deepcopy to avoid referring the original list as we might need the values again
        __colours = copy.deepcopy(term_colours)
        for p in range(players_count):
            if not __colours:
                __colours = copy.deepcopy(term_colours)
            players.append(Player(player_count, __colours.pop()))
            player_count += 1
        for c in range(cpu_count):
            if not __colours:
                __colours = copy.deepcopy(term_colours)
            players.append(Player(player_count, __colours.pop(), cpu=True))
            player_count += 1
        return cls(Deck.create_fresh_deck(), players)

    def initial_hand(self) -> None:
        """
        Give out initial hand to players and dealer
        :return: None
        """
        for x in range(2):
            for player in self.players:
                player.hand.add_card(self.deck.get_random_card())

    def hit(self, player: int) -> Optional[Card]:
        """
        Draw a card for a player
        :param player: player number
        :return: card drawn
        """
        player -= 1
        card = self.deck.get_random_card()
        if card:  # If card is not None
            self.players[player].hand.add_card(card)
        return card

    # def stand(self, player: int) -> None:
    #     """
    #     Stand (do nothing to a player's hand)
    #     :param player: player number
    #     :return: None
    #     """
    #     # This is here symbolically, as we don't need to do anything here (aka ignore me)
    #     pass

    def __getitem__(self, player_int):
        return self.players[player_int]

    def __iter__(self):
        """Start iterator on object"""
        self.__iter_player = 0
        return self

    def __next__(self):
        """Get next item in iteration"""
        if self.__iter_player < len(self.players):
            player = self.players[self.__iter_player]
            self.__iter_player += 1
            return player
        else:
            raise StopIteration
