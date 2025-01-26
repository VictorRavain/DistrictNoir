from typing import List
import random
from .card import Card

class Player:
    def __init__(self, name):
        self.name = name
        self.hand: List[Card] = []  # The player's hand of cards
        self.collected_cards: List[Card] = []   # Cards collected during the game
        self.score = 0  # Player's current score
        self.has_take = False
    
    def play_card(self):
        """Play a card from hand."""
        choosed_card = random.choice(self.hand)
        self.hand.remove(choosed_card)
        return choosed_card
    
    def take_cards(self, cards : List[Card]):   
        """Collect cards from the center line."""
        self.collected_cards.extend(cards)

    def draw_cards(self, cards : List[Card]):   
        """Collect cards from the center line."""
        self.hand.extend(cards)