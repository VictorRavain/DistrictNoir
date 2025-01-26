import random
from typing import List
from .card import Card

class Deck:
    def __init__(self):
        self.deck: List[Card] = self._initialize_deck()
        random.shuffle(self.deck)
        self.bin: List[Card] = self.pick_random_cards(3)

    def _initialize_deck(self):
        """Initialize the deck with the 45 deck."""
        deck = []

        # Add Soutien card (26 total)
        soutien_values = {5: 5, 6: 6, 7: 7, 8: 8}
        for value, count in soutien_values.items():
            deck.extend([Card("SOUTIEN", value) for _ in range(count)])

        # Add Alliance card (7 total)
        deck.extend([Card("ALLIANCE", 4) for _ in range(1)]) # Add 1 Alliance +4 card
        deck.extend([Card("ALLIANCE", 3) for _ in range(2)]) # Add 2 Alliance +3 card
        deck.extend([Card("ALLIANCE", 2) for _ in range(4)]) # Add 4 Alliance +2 card

        # Add Trahison card (9 total)
        deck.extend([Card("TRAHISON", -3) for _ in range(2)]) # Add 2 Trahison -3 card
        deck.extend([Card("TRAHISON", -2) for _ in range(3)]) # Add 3 Trahison -2 card
        deck.extend([Card("TRAHISON", -1) for _ in range(4)]) # Add 4 Trahison -1 card
        
        # Add Ville card (3 total)
        deck.extend([Card("VILLE", 0) for _ in range(3)])

        return deck

    def pick_random_cards(self, count=1):
        """Remove a specified number of deck randomly from the deck."""
        if len(self.deck) >= count:
            removed_cards = random.sample(self.deck, count)
            for card in removed_cards:
                self.deck.remove(card)
            return removed_cards
        else:
            raise ValueError("Not enough card in the deck to remove.")