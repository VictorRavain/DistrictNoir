import random
import inquirer
import string
from collections import Counter
from typing import List
from .deck import Deck
from .card import Card
from .player import Player

class Game:
    def __init__(self, game_id: int, name1: string, name2: string):
        self.game_id = game_id
        self.player1 = Player(name1)
        self.player2 = Player(name2)
        self.deck = Deck()
        self.game_line: List[Card] = []  # The cards in the center line
    
    def start_game(self):
        """Start the game and handle game flow."""
        self.game_log = {"game_id": 1, "steps": [], "final_result": {}}
        self.game_line.extend(self.deck.pick_random_cards(2))
        # Manche 1 :
        self.play_set()
        # Manche 2 :
        self.play_set()
        # Manche 3 :
        self.play_set()
        # Manche 4 :
        self.play_set()
        self.end_set()
        return self.game_log

    def play_set(self):
        """Play a single set in the game."""
        # Log the beginning of the set
        set_log = {
            "set_id": len(self.game_log["steps"]) + 1,
            "initial_state": {
                "player1_hand": self.player1.hand.copy(),
                "player2_hand": self.player2.hand.copy(),
                "game_line": self.game_line.copy()
            },
            "actions": []
        }

        # Deal initial cards
        self.player1.draw_cards(self.deck.pick_random_cards(5))
        self.player2.draw_cards(self.deck.pick_random_cards(5))

        # Reset 'has_take' for both players
        self.player1.has_take = False
        self.player2.has_take = False

        # Play until a set-ending condition is met
        while not self.check_city_victory() and not self.is_set_over():
            # Player 1's turn
            set_log["actions"].append(self.play_turn(self.player1))
            # Player 2's turn
            set_log["actions"].append(self.play_turn(self.player2))
    
        # Append the set log to the game log
        self.game_log["steps"].append(set_log)
    
    def play_turn(self, player: Player):
        """Handle the actions taken by the player on their turn."""
        turn_log = {"player": player.name, "action": "", "result": {}}

        print(f"\n{player.name}'s Turn!")
        print(f"Your hand: {player.hand}")
        print(f"Game line: {self.game_line}")

        # Show a menu to let the player choose an action
        action = player.choose_action()
                
        if action=="play":
            played_card = player.choose_card_to_play()
            self.game_line.append(played_card)
            print(f"You played: {played_card}")
            turn_log["action"] = "play"
            turn_log["result"] = {
                "played_card": played_card,
                "updated_game_line": self.game_line.copy()
            }
        elif action == "take":
            self.game_line = player.collect_cards(self.game_line)
            player.has_take = True
            print(f"You collected cards. Your collected cards: {player.collected_cards}")
            turn_log["action"] = "take"
            turn_log["result"] = {
                "collected_cards": player.collected_cards.copy()
            }

        return turn_log

    def is_set_over(self):
        """
        Check if the set is over. 
        The set ends when all players have no more cards in their hands and has taken cards.
        """
        return all(len(player.hand) == 0 and player.has_take for player in [self.player1, self.player2]) 
    
    def end_set(self):
        """
        Handle the end of the set.
        Calculate scores and determine the winner.
        Return the scores and the detail of player's collected card.
        """
        self.player1.score = self.calculate_score(self.player1, self.player2)
        self.player2.score = self.calculate_score(self.player2, self.player1)

        winner = ""
        if self.player1.score > self.player2.score:
            winner = self.player1.name
        elif self.player2.score > self.player1.score:
            winner = self.player2.name

        print(f"{self.player1.name}'s score: {self.player1.score}")
        print(f"{self.player2.name}'s score: {self.player2.score}")
        print(f"{winner} wins the game!")
        
        self.game_log["final_result"] = {
            "player1_score": self.player1.score,
            "player2_score": self.player2.score,
            "winner": winner
        }

    def calculate_score(self, player: Player, opponent: Player):
        """
        Calculate the player's score based on the endgame rules:
        1. Majority on each type of SOUTIEN grants points equal to the value on the card.
        2. A set of 4 different types of SOUTIENS grants 5 additional points.
        3. Add or subtract points based on ALLIANCE and TRAHISON cards.
        4. Exclude VILLE cards from scoring.
        """
        soutien_points = 0
        extra_points = 0
        alliance_trahison_points = 0
        
        # Filter collected cards into categories
        soutien_cards = [card for card in player.collected_cards if card.card_type == "SOUTIEN"]
        opponent_soutien_cards = [card for card in opponent.collected_cards if card.card_type == "SOUTIEN"]
        alliance_trahison_cards = [card for card in player.collected_cards if card.card_type in ["ALLIANCE", "TRAHISON"]]
        
        # Count each type of SOUTIEN for both players
        player_soutien_count = Counter(card.value for card in soutien_cards)
        opponent_soutien_count = Counter(card.value for card in opponent_soutien_cards)
        
        # Determine majority for each type of SOUTIEN
        for subtype, count in player_soutien_count.items():
            opponent_count = opponent_soutien_count.get(subtype, 0)
            if count > opponent_count:
                # Player has majority
                soutien_points += int(subtype)  # Use the card's value (subtype represents value)
            elif count == opponent_count:
                # No points for ties
                continue

        extra_points += self.calculate_bonus_points_for_sets(player_soutien_count)

        # Calculate ALLIANCE and TRAHISON points
        for card in alliance_trahison_cards:
            alliance_trahison_points += card.value  # Add positive or negative based on card value

        # Total score for the player
        total_score = soutien_points + extra_points + alliance_trahison_points
        return total_score

    def calculate_bonus_points_for_sets(self, player_soutien_count):
        extra_points = 0

        # Continue while at least 4 unique types of SOUTIEN are available
        while len(player_soutien_count) >= 4:
            # Deduct one card from each unique type in the set
            for subtype in list(player_soutien_count.keys()):  # Use list() to avoid RuntimeError during iteration
                player_soutien_count[subtype] -= 1
                if player_soutien_count[subtype] == 0:
                    del player_soutien_count[subtype]  # Remove the type if its count reaches 0
            
            # Add 5 points for the completed set of 4 unique cards
            extra_points += 5

        return extra_points

    def check_city_victory(self):
        for player in [self.player1, self.player2]:
            city_count = sum(1 for card in player.collected_cards if card.card_type == "VILLE")
            if city_count >= 3:
                return True
        return False