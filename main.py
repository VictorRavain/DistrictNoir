from src.game import Game
from collections import Counter
import time

def simulate_games(num_games: int):
    scores = []
    highest_single_score = 0
    lowest_single_score = 0
    highest_score_info = None
    lowest_score_info = None
    highest_single_score_info = None
    lowest_single_score_info = None
    total_time = 0  # Track the total time taken for all games

    for _ in range(num_games):
        start_time = time.time()

        game = Game("Victor", "Julie")
        result = game.start_game()  # Start the game and get scores

        end_time = time.time()
        elapsed_time = end_time - start_time  # Calculate time taken for the game
        total_time += elapsed_time  # Accumulate total time

        player1_score, player1_cards, player2_score, player2_cards = result
        
        # Normalize the score by sorting the tuple
        normalized_score = tuple(sorted([player1_score, player2_score]))  
        scores.append((normalized_score, player1_score, player1_cards, player2_score, player2_cards))  # Store normalized scores and card info
        
        # Track the highest single score
        highest_single_score = max(highest_single_score, player1_score, player2_score)
        lowest_single_score = min(lowest_single_score, player1_score, player2_score)

        # Track the highest and lowest total scores with their card info
        total_score = player1_score + player2_score
        if highest_score_info is None or total_score > highest_score_info[0]:
            highest_score_info = (total_score, player1_score, player1_cards, player2_score, player2_cards)
        if lowest_score_info is None or total_score < lowest_score_info[0]:
            lowest_score_info = (total_score, player1_score, player1_cards, player2_score, player2_cards)
        if highest_single_score_info is None or highest_single_score < highest_single_score_info[0]:
            highest_single_score_info = (highest_single_score, player1_score, player1_cards, player2_score, player2_cards)
        if lowest_single_score_info is None or lowest_single_score < lowest_single_score_info[0]:
            lowest_single_score_info = (lowest_single_score, player1_score, player1_cards, player2_score, player2_cards)

    # Count occurrences of each normalized score
    score_distribution = Counter([score for score, _, _, _, _ in scores])
    most_probable = score_distribution.most_common()
    least_probable = score_distribution.most_common()[-10:]  # Last 10 are least probable

    print("Most probable scores (order does not matter):")
    for score, count in most_probable[:10]:  # Limit to 10 most probable
        print(f"Score {score}: {count} times")

    print("\nLeast probable scores (order does not matter):")
    for score, count in least_probable:  # Print the 10 least probable
        print(f"Score {score}: {count} times")

    print("\nHighest total score:", highest_score_info[0], 
          f"with player 1 score: {highest_score_info[1]} and player 2 score: {highest_score_info[3]}")
    # print("Player 1 cards:", highest_score_info[2])
    # print("Player 2 cards:", highest_score_info[4])

    print("\nLowest total score:", lowest_score_info[0], 
          f"with player 1 score: {lowest_score_info[1]} and player 2 score: {lowest_score_info[3]}")
    # print("Player 1 cards:", lowest_score_info[2])
    # print("Player 2 cards:", lowest_score_info[4])

    print("\nHighest single score achieved in any game:", highest_single_score)
    # print("Player 1 cards:", highest_single_score_info[2])
    # print("Player 2 cards:", highest_single_score_info[4])

    print("\nLowest single score achieved in any game:", lowest_single_score)
    # print("Player 1 cards:", lowest_single_score_info[2])
    # print("Player 2 cards:", lowest_single_score_info[4])

    print(f"\nTotal time taken for {num_games} games: {total_time:.4f} seconds")
    print(f"Average time per game: {total_time / num_games:.8f} seconds")

if __name__ == "__main__":
    simulate_games(100000)  # Simulate 10000 games
