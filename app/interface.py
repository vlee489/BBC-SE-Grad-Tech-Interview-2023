"""
Handles all the interfacing for the game in Blackjack to make playable
"""
from app.game import Game
from app.cpu import cpu_decision
from termcolor import cprint


class Interface:
    players: int
    cpus: int
    dealer: bool
    game: Game

    def __init__(self, players: int, cpus: int):
        self.players = players
        self.cpus = cpus
        cprint(f"Setting up game & dealing hand")
        self.game = Game.create_game(players, cpus)
        self.game.initial_hand()
        self.print_players_cards()
        self.play()

    def play(self):
        while True:
            # Announce who's out from last round
            for player in self.game:
                if not player.hand.valid() and not player.show_bust:
                    cprint(f"Player {player.player_num} is Bust at {int(player.hand)} and is out", player.text_colour)
                    player.show_bust = True
                elif player.hand.valid():
                    cprint(f"Player {player.player_num} is valid at {int(player.hand)}", player.text_colour)

            # TODO: Check players if deck is gone

            # Check there's a player with a valid hand
            # Go through all players and count number of people with valid hands
            player_with_valid_hands = 0
            for player in self.game:
                if player.hand.valid():
                    player_with_valid_hands += 1
            if player_with_valid_hands == 1:
                # If only one player has a valid hand, find player and announce they've won
                for player in self.game:
                    if player.hand.valid():
                        cprint(f"Player {player.player_num} has won with a hand of {int(player.hand)}")
                return
            elif player_with_valid_hands < 1:
                # If no valid hands, everyone went bust
                print("You all went Bust >.<")
                return
            # else allow game to continue on

            # Allow Players to choose cards
            for x in range(self.players):
                if self.game[x].hand.valid():
                    p_choice = self.player_input(x)
                    if p_choice:
                        card = self.game.hit(x)
                        cprint(f"player {x + 1} choose hit and drew: {card}")

            # Allow CPUs to choose card
            for x in range(self.cpus):
                cpu = x + self.players
                cpu_player = self.game[cpu]
                if cpu_player.hand.valid():
                    if cpu_decision(self.game[cpu].hand, int(self.game.deck)):
                        self.game.hit(cpu)
                        cprint(f"CPU player {cpu} decided to HIT and drew a card!", cpu_player.text_colour)
                    else:
                        cprint(f"CPU player {cpu} decided to STAND", cpu_player.text_colour)
            # Print cards players have
            self.print_players_cards()

    def print_players_cards(self):
        """Show stand of players and not CPUs"""
        for player_int in range(self.players):
            player = self.game[player_int]
            if player.hand.valid() or (not player.hand.valid() and not player.show_bust):
                cprint(f"---Cards for player {player_int + 1}---", player.text_colour)
                for card in player.hand:
                    cprint(card, player.text_colour)
                cprint(f"Your current total is: {int(player.hand)}", player.text_colour)
                if not player.hand.valid():
                    cprint(f"You've gone bust and are out!", player.text_colour)
        print("---")

    @staticmethod
    def player_input(player: int) -> bool:
        """
        Takes input from player
        :param player: player number
        :return: bool True = Hit, False = Stand
        """
        while True:
            choice = input(f"Player {player} please choose to \"hit\" or \"stand\": ")
            match choice.upper():
                case "HIT" | "H":
                    return True
                case "STAND" | "S":
                    return False
                case _:
                    print("Invalid choice, choose again between \"hit\" or \"stand\"")
