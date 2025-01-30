import argparse
import deck_creator
from game import game_loop
from classes import Player,Deck
def main():
    parser = argparse.ArgumentParser(description="Start a new card game.")
    parser.add_argument(
        "scoring_method",
        type=str,
        choices=["points", "battle", "p", "b"],
        default="points",
        help="Choose the scoring method: points (p) or battle (b) (default: points).",
    )
    parser.add_argument(
        "player_a_type",
        type=str,
        choices=["human", "static_ai", "monte_carlo_ai", "h", "s", "m"],
        default="static_ai",
        help="Specify the type for Player A: human (h), static_ai (s), or monte_carlo_ai (m) (default: static_ai).",
    )
    parser.add_argument(
        "player_b_type",
        type=str,
        choices=["human", "static_ai", "monte_carlo_ai", "h", "s", "m"],
        default="human",
        help="Specify the type for Player B: human (h), static_ai (s), or monte_carlo_ai (m) (default: human).",
    )
    args = parser.parse_args()
    args = parser.parse_args()
    deck = Deck(deck_creator.read_card_data("cards.json")["cards"])
    player_a = Player("Player A", deck)
    player_b = Player("Player B", deck)
    game_loop(player_a,player_b,scoring_arg=args.scoring_method,player_1=args.player_a_type,player_2=args.player_b_type)

if __name__ == "__main__":
    main()