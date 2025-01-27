import json
from src.game import Game
from src.card import Card, CardType

import json

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Card):
            return {"card_type": obj.card_type, "value": obj.value}
        elif isinstance(obj, CardType):
            return obj.value
        return super().default(obj)

def simulate_games(num_games: int):

    for game_id in range(num_games):
        game = Game(game_id, "Victor", "Julie")
        result = game.start_game()  # Start the game and get scores

        save_game_log(result)

def save_game_log(game_log, filename="game_log.json"):
    with open(filename, "w") as f:
        json.dump(game_log, f, indent=4, cls=CustomJSONEncoder)
        
if __name__ == "__main__":
    simulate_games(1)  # Simulate "n" games
