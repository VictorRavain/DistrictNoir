from typing import List
import random
import inquirer
from .card import Card

class Player:
    def __init__(self, name):
        self.name = name
        self.hand: List[Card] = []  # The player's hand of cards
        self.collected_cards: List[Card] = []   # Cards collected during the game
        self.score = 0  # Player's current score
        self.has_take = False
    
    def play_random_card(self):
        """Play a card from hand."""
        choosed_card = random.choice(self.hand)
        self.hand.remove(choosed_card)
        return choosed_card
    
    def choose_action(self):
        # Show a menu to let the player choose an action
        actions = ["play", "take"]

        # Player already took; only "play" is possible
        if self.has_take:  
            actions = ["play"]

        # If the player's hand is empty, they must take
        if len(self.hand) == 0:
            actions = ["take"]
        
        action = inquirer.list_input(
            "Choose your action:",
            choices=actions
        )
        return action
    
    def choose_card_to_play(self):
        """
        Allow the player to choose a card from their hand to play.
        """
        # Create a menu for card selection
        card_choices = [f"{idx + 1}: {card}" for idx, card in enumerate(self.hand)]
        selected_card_str = inquirer.list_input(
            "Choose a card to play:",
            choices=card_choices
        )
        
        # Extract the card index from the string
        selected_index = int(selected_card_str.split(":")[0]) - 1
        selected_card = self.hand.pop(selected_index)
        return selected_card
    
    def collect_cards(self, game_line: List[Card]):
        """
        Allow the player to take up to the last 5 cards from the center line.
        If there are fewer than 5 cards in the game line, take all of them.
        """
        # Determine the number of cards to take (max 5 or all available)
        num_cards_to_take = min(5, len(game_line))
        # Extract the last 'num_cards_to_take' cards
        cards_to_take = game_line[-num_cards_to_take:]
        # Remove the extracted cards from the game line
        game_line = game_line[:-num_cards_to_take]
        # Add the cards to the player's collected cards
        self.take_cards(cards_to_take)
        return game_line

    def take_cards(self, cards : List[Card]):   
        """Collect cards from the center line."""
        self.collected_cards.extend(cards)

    def draw_cards(self, cards : List[Card]):   
        """Collect cards from the center line."""
        self.hand.extend(cards)