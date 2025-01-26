import string
from collections import Counter
from typing import List
from .deck import Deck
from .card import Card
from .player import Player

class Game:
    def __init__(self, name1: string, name2: string):
        self.player1 = Player(name1)
        self.player2 = Player(name2)
        self.deck = Deck()
        self.game_line: List[Card] = []  # The cards in the center line
    
    def start_game(self):
        """Start the game and handle game flow."""
        self.game_line.extend(self.deck.pick_random_cards(2))
        # Manche 1 :
        self.play_set()
        # Manche 2 :
        self.play_set()
        # Manche 3 :
        self.play_set()
        # Manche 4 :
        self.play_set()
        return self.end_set()

    def play_set(self):
        self.player1.draw_cards(self.deck.pick_random_cards(5))
        self.player2.draw_cards(self.deck.pick_random_cards(5))
        self.player1.has_take = False
        self.player2.has_take = False
        while not self.check_city_victory() and not self.is_set_over():
            self.play_turn(self.player1, "play")
            self.play_turn(self.player2, "play")
        return
    
    def play_turn(self, player: Player, action: string):
        """Handle the actions taken by the player on their turn."""
        if len(player.hand) == 0: # If player has no more card available, he has to take
            action = "take"

        if action=="play":
            played_card = player.play_card()
            self.game_line.append(played_card)
            # print("player :",player.name, "played :",played_card)
        elif action == "take":
            self.take_cards_from_game_line(player)
            player.has_take = True
            # print("Player's card", player.name,":", player.collected_cards)
        else:
            print("Invalid action. Choose either 'play' or 'take'.")

    def take_cards_from_game_line(self, player: Player):
        """
        Allow the player to take up to the last 5 cards from the center line.
        If there are fewer than 5 cards in the game line, take all of them.
        """
        # Determine the number of cards to take (max 5 or all available)
        num_cards_to_take = min(5, len(self.game_line))
        # Extract the last 'num_cards_to_take' cards
        cards_to_take = self.game_line[-num_cards_to_take:]
        # Remove the extracted cards from the game line
        self.game_line = self.game_line[:-num_cards_to_take]
        # Add the cards to the player's collected cards
        player.take_cards(cards_to_take)

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
        self.player1_score = self.calculate_score(self.player1, self.player2)
        self.player2_score = self.calculate_score(self.player2, self.player1)

        # print(f"{self.player1.name}'s score: {self.player1_score}")
        # print(f"{self.player2.name}'s score: {self.player2_score}")

        # if self.player1_score > self.player2_score:
        #     print(f"{self.player1.name} wins the game!")
        #     pass
        # elif self.player2_score > self.player1_score:
        #     print(f"{self.player2.name} wins the game!")
        #     pass
        
        return [self.player1_score, self.player1.collected_cards, self.player2_score, self.player2.collected_cards]

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