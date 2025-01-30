import json
import random
import matplotlib.pyplot as plt
import tuning
import numpy as np
from collections import defaultdict

def generate_stat(mean, std_dev, min_val=1, max_val=100):
    """Generate a stat with a normal distribution, clamped between min_val and max_val."""
    return max(min(int(random.gauss(mean, std_dev)), max_val), min_val)

def calculate_total_in_deck(stats):
    """Calculate the number of appearances based on stat extremes."""
    # Higher extremes (closer to min_val or max_val) make the card rarer
    z_scores = []
    
    for stat, value in stats.items():
        if stat in tuning.deck_stats:
            mean, std = tuning.deck_stats[stat]
            z_score = (value - mean) / std
            z_scores.append(abs(z_score))
    
    if not z_scores:
        return tuning.max_appearances  # Default to most common if no valid stats
    
    Z_total = np.max(z_scores)
    
    # Normalize Z_total into the appearance range
    scale = (tuning.max_appearances - tuning.min_appearances) / 4.0
    appearances = tuning.max_appearances - round(Z_total * scale)
    
    return max(tuning.min_appearances, min(tuning.max_appearances, appearances))

def generate_card_data(total_appearances=100, variations_per_card=3):
    """Generate card data ensuring total appearances across all cards sum to total_appearances."""
    cards = {}
    remaining_appearances = total_appearances
    card_id = 1

    while remaining_appearances > 0:
        card_name = f"Card {card_id}"
        variations = {}
        for variation_id in range(1, variations_per_card + 1):
            variation_name = f"{card_name} Variation {variation_id}"
            stats = {
                "Head": generate_stat(mean=tuning.deck_stats["Head"][0],std_dev=tuning.deck_stats["Head"][1]),
                "Heart": generate_stat(mean=tuning.deck_stats["Heart"][0],std_dev=tuning.deck_stats["Heart"][1]),
                "Temper": generate_stat(mean=tuning.deck_stats["Temper"][0],std_dev=tuning.deck_stats["Temper"][1]),
                "Skin": generate_stat(mean=tuning.deck_stats["Skin"][0],std_dev=tuning.deck_stats["Skin"][1]),
                "Speed": generate_stat(mean=tuning.deck_stats["Speed"][0],std_dev=tuning.deck_stats["Speed"][1]),
                "Strength": generate_stat(mean=tuning.deck_stats["Strength"][0],std_dev=tuning.deck_stats["Strength"][1]),
                "Special": generate_stat(mean=tuning.deck_stats["Special"][0],std_dev=tuning.deck_stats["Special"][1])
            }
            variations[str(variation_id)] = {
                "name": variation_name,
                "stats": stats
            }
        # Calculate appearances for this card based on stats, but ensure it does not exceed remaining_appearances
        total_in_deck = min(calculate_total_in_deck(stats), remaining_appearances)
        remaining_appearances -= total_in_deck

        cards[f"card{card_id}"] = {
            "name": card_name,
            "total_in_deck": total_in_deck,
            "variations": variations
        }

        card_id += 1

    return {"cards": cards}


# print(f"Card data has been generated and saved to {output_file}.")
def read_card_data(file_path):
    """Read card data from a JSON file."""
    with open(file_path, "r") as f:
        return json.load(f)

def extract_max_stat_data(cards):
    """Extract the highest possible stat for each card across all variations."""
    stats_data = defaultdict(list)
    for card in cards.values():
        max_stats = defaultdict(int)
        for variation in card["variations"].values():
            for stat, value in variation["stats"].items():
                max_stats[stat] = max(max_stats[stat], value)
        for stat, value in max_stats.items():
            stats_data[stat].append(value)
    return stats_data

def plot_stat_distributions(stats_data):
    """Generate and display distribution graphs for each stat."""
    for stat, values in stats_data.items():
        plt.figure()
        plt.hist(values, bins=range(1, 102, 5), edgecolor="black", alpha=0.7)
        plt.title(f"Distribution of {stat}")
        plt.xlabel(stat)
        plt.ylabel("Frequency")
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.show()

def generate_deck():
    card_data = generate_card_data(total_appearances=tuning.total_appearances, variations_per_card=tuning.variations_per_card)
    output_file = "cards.json"

    with open(output_file, "w") as f:
        json.dump(card_data, f, indent=4)

def show_deck_distribution():
    file_path = "cards.json"  # Adjust the path if needed
    card_data = read_card_data(file_path)
    stats_data = extract_max_stat_data(card_data["cards"])
    plot_stat_distributions(stats_data)