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
            print("---")

            # Check deck is gone
            if len(self.game.deck) == 0:
                self.out_of_cards_routine()

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

            # Gp through each player and allow them to make a move
            for player in self.game:
                # Check deck is gone
                if len(self.game.deck) == 0:
                    self.out_of_cards_routine()

                if not player.cpu:  # If human player
                    if player.hand.valid():
                        p_choice = self.player_input(player.player_num)  # Take human input
                        if p_choice:  # If they chose to Hit
                            card = self.game.hit(player.player_num)  # Draw card
                            cprint(f"player {player.player_num} choose hit and drew: {card}", player.text_colour)
                else:  # is a CPU
                    if player.hand.valid():
                        if cpu_decision(player.hand, int(self.game.deck)):  # CPU chooses to hit or not
                            self.game.hit(player.player_num)  # Draw card
                            cprint(f"CPU player {player.player_num} decided to HIT and drew a card!",
                                   player.text_colour)
                        else:
                            cprint(f"CPU player {player.player_num} decided to STAND", player.text_colour)

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

    def out_of_cards_routine(self):
        """Runs when there's no cards left in deck"""
        # if deck has no cards
        closest_player = []  # Holds players with the highest value
        closest_hand_value = 0  # Holds the highest hand value
        for player in self.game:
            if player.hand.valid():
                if int(player.hand) > closest_hand_value:
                    # If the hand value is greater than what we already have
                    closest_hand_value = int(player.hand)  # Set the newest highest value
                    closest_player = [player]  # Overwrite the list with the single highest value
                elif int(player.hand) == closest_hand_value:
                    # Is the value is the same as our current highest value we append it to the list of players
                    # with tha value
                    closest_player.append(player)
        if closest_player:
            # Forms a string with the player number of the players with the highest value
            player_num = ""
            for player in closest_player:
                player_num += f"{player.player_num}, "
            print("Deck is now empty!")
            print(f"Players closest to 21 are {player_num[:-2]} with a score of {closest_hand_value}")
            exit(0)  # exit game
        else:
            # Shows message is not one has a valid hand when deck is empty
            print("Deck is now empty!")
            print("No players have a valid deck >.<")
            exit(0)  # exit game

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
