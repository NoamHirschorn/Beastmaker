import random
from classes import Player
import tuning
import scoring
from scipy.stats import norm
import copy


def calculate_percentile(stat_value, mean, std_dev):
    """Calculate the percentile for a given stat value based on the mean and standard deviation."""
    return norm.cdf(stat_value, loc=mean, scale=std_dev) * 100

def ai_choose_play(ai_player_hand, available_slots,remaining_deck_stats):
    """Choose the best slot and variation for the AI player to play the card."""
    if ai_player_hand is None:
        print("AI has no card in hand to play.")
        return None

    if not available_slots:
        print("AI has no available slots to play the card.")
        return None

    # Find the max value for each stat across all variations
    max_values = {}
    best_variation_for_stat = {}
    for variation_name, variation_data in ai_player_hand["variations"].items():
        for stat, value in variation_data["stats"].items():
            if stat not in max_values or value > max_values[stat]:
                max_values[stat] = value
                best_variation_for_stat[stat] = variation_name

    best_choice = None
    best_percentile = -1

    for slot in available_slots:
        stat_value = max_values[slot]
        mean, std_dev = remaining_deck_stats[slot]
        percentile = calculate_percentile(stat_value, mean, std_dev)

        if percentile > best_percentile:
            best_percentile = percentile
            best_choice = (slot, best_variation_for_stat[slot])

    return best_choice



def simulate_game(ai_player, opponent,deck, score_by_points,num_simulations=100):
    """Simulate the game to estimate the expected outcome of a move."""
    ai_score = 0
    for _ in range(num_simulations):
        # Copy current board states
        simulated_ai_board = copy.deepcopy(ai_player.board)
        simulated_opponent_board = copy.deepcopy(opponent.board)
        simulated_ai_hand = ai_player.hand
        simulated_opponent_hand = opponent.hand
        while True:
            
            # Simulate AI move
            if simulated_ai_hand is None and deck:
                simulated_ai_hand = random.choice(deck.cards)
            available_slots = [slot for slot, card in simulated_ai_board.items() if card is None]
            if available_slots and simulated_ai_hand is not None:
                round = 7-len(available_slots)
                epsilon = tuning.epsilon_start-round*(tuning.epsilon_start-tuning.epsilon_end)/7
                if(random.random()<epsilon):
                    simulated_ai_hand,simulated_ai_board=play_random_card(simulated_ai_hand,simulated_ai_board,available_slots)
                else:
                    chosen_slot,variation=ai_choose_play(simulated_ai_hand,available_slots,tuning.deck_stats)
                    simulated_ai_board[chosen_slot] = {
                    "card_name": simulated_ai_hand["name"],
                    "variation": variation,
                    "stats": simulated_ai_hand["variations"][variation]["stats"]
                    }
                simulated_ai_hand = None

            if (not any(slot is None for slot in simulated_ai_board.values()) and not any(slot is None for slot in simulated_opponent_board.values())):
                break
            # Simulate Opponent move
            if simulated_opponent_hand is None and deck:
                simulated_opponent_hand = random.choice(deck.cards)
            available_slots = [slot for slot, card in simulated_opponent_board.items() if card is None]
            if available_slots and simulated_opponent_hand is not None:
                round = 7-len(available_slots)
                epsilon = tuning.epsilon_start-round*(tuning.epsilon_start-tuning.epsilon_end)/7
                if(random.random()<epsilon):
                     simulated_opponent_hand,simulated_opponent_board=play_random_card(simulated_opponent_hand,simulated_opponent_board,available_slots)
                else:
                    chosen_slot,variation=ai_choose_play(simulated_opponent_hand,available_slots,tuning.deck_stats)
                    simulated_opponent_board[chosen_slot] = {
                    "card_name": simulated_opponent_hand["name"],
                    "variation": variation,
                    "stats": simulated_opponent_hand["variations"][variation]["stats"]
                    }
                simulated_ai_hand = None
            if (not any(slot is None for slot in simulated_ai_board.values()) and not any(slot is None for slot in simulated_opponent_board.values())):
                break

        simulated_ai_stats = {stat: card["stats"][stat] for stat, card in simulated_ai_board.items() if card is not None}
        simulated_opponent_stats = {stat: card["stats"][stat] for stat, card in simulated_opponent_board.items() if card is not None}
        if(score_by_points):
            result =scoring.determine_winner_scoring(simulated_ai_stats, simulated_opponent_stats)["winner"]
        else:
            result =scoring.estimate_battle(simulated_ai_stats, simulated_opponent_stats)["winner"]
        if result == "Player A":
            ai_score += 1
        elif result == "Draw":
            ai_score += 0.5
                    

    return ai_score / num_simulations


def monte_carlo_ai(ai_player, opponent, remaining_deck, score_by_points,num_simulations=100):
    """Choose the best move for the AI using Monte Carlo simulations."""
    if ai_player.hand is None:
        print("AI has no card in hand to play.")
        return

    available_slots = [slot for slot, card in ai_player.board.items() if card is None]
    if not available_slots:
        print("AI has no available slots to play the card.")
        return

    max_values = {}
    best_variation_for_stat = {}
    for variation_name, variation_data in ai_player.hand["variations"].items():
        for stat, value in variation_data["stats"].items():
            if stat not in max_values or value > max_values[stat]:
                max_values[stat] = value
                best_variation_for_stat[stat] = variation_name

    best_choice = None
    best_score = -1

    for slot in available_slots:
        variation = best_variation_for_stat[slot]

        # Simulate the game for this move
        ai_player.board[slot] = {
            "card_name": ai_player.hand["name"],
            "variation": variation,
            "stats": ai_player.hand["variations"][variation]["stats"]
        }

        score = simulate_game(ai_player, opponent, remaining_deck,score_by_points, num_simulations)

        if score > best_score:
            best_score = score
            best_choice = (slot, variation)

        # Reset the board
        ai_player.board[slot] = None

    return best_choice
        

def play_random_card(hand,board,available_slots):
    if hand is not None:
        slot = random.choice(available_slots)
        variation = random.choice(list(hand["variations"].keys()))
        board[slot] = {
                    "card_name": hand["name"],
                    "variation": variation,
                    "stats": hand["variations"][variation]["stats"]
                    }
        hand = None
    return hand,board



