from enum import Enum
from typing import List

class CardType(Enum):
    SOUTIEN = "Soutien"
    ALLIANCE = "Alliance"
    TRAHISON = "Trahison"
    VILLE = "Ville"

class Card:
    def __init__(self, card_type: CardType, value: int = None):
        self.card_type = card_type  # SOUTIEN, ALLIANCE, TRAHISON, or VILLE
        self.value = value          # The value of the card (5, 6, 7, 8 for SOUTIEN)
    
    def __repr__(self):
        return f"{self.card_type} ({self.value})"

    def is_soutien(self):
        return self.card_type == CardType.SOUTIEN

    def is_alliance(self):
        return self.card_type == CardType.ALLIANCE

    def is_trahison(self):
        return self.card_type == CardType.TRAHISON

    def is_ville(self):
        return self.card_type == CardType.VILLE
