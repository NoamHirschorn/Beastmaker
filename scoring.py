import random
import numpy as np
import tuning
def calculate_score(winner_stat, loser_stat):
    """Calculate the score for the winner based on the margin of victory and the loser's stat."""
    if winner_stat <= loser_stat:
        return 0
    margin = winner_stat - loser_stat
    scaling_factor = 1/ (loser_stat + 1)  # Avoid division by zero and reduce punishment for higher stats
    score = margin*(scaling_factor**tuning.scaling_factor_strength)
    return score*100 #scale scores so easier to track/make inetgers

def determine_winner_scoring(player_a_stats, player_b_stats):
    """Determine the winner based on the stats of two players."""
    categories = ["Head", "Heart", "Temper", "Skin", "Speed", "Strength", "Special"]
    player_a_points = {category: 0 for category in categories}
    player_b_points = {category: 0 for category in categories}

    for category in categories:
        if category in ["Strength", "Skin"]:
            # Strength vs Skin interactions
            if category == "Strength":
                player_a_score = calculate_score(player_a_stats[category], player_b_stats["Skin"])
                player_b_score = calculate_score(player_b_stats[category], player_a_stats["Skin"])
            else:  # category == "Skin"
                player_a_score = calculate_score(player_a_stats[category], player_b_stats["Strength"])
                player_b_score = calculate_score(player_b_stats[category], player_a_stats["Strength"])
        else:
            # Normal case: direct stat comparison
            player_a_score = calculate_score(player_a_stats[category], player_b_stats[category])
            player_b_score = calculate_score(player_b_stats[category], player_a_stats[category])

        player_a_points[category] = player_a_score
        player_b_points[category] = player_b_score

    # Calculate total scores
    total_a = sum(player_a_points.values())
    total_b = sum(player_b_points.values())

    # Determine winner
    if total_a > total_b:
        winner = "Player A"
    elif total_b > total_a:
        winner = "Player B"
    else:
        winner = "Draw"

    return {
        "margin": total_a-total_b,
        "winner": winner,
        "player_a_points": player_a_points,
        "player_b_points": player_b_points,
        "total_a": total_a,
        "total_b": total_b
    }

def calculate_attack(strength, opposing_skin, speed, temper, special, head):
    crit = False
    """Calculate the attack for a single round."""
    base_attack = random.uniform(tuning.base_dmg+tuning.random_range, tuning.base_dmg-tuning.random_range) + strength - opposing_skin
    effective_attack = base_attack/tuning.base_attack_divisor

    # Chance to use special skill
    if random.random() < (head / tuning.special_skill_divisor):
        effective_attack =effective_attack+(special *tuning.special_scaling_factor)
        crit = True

    # Modify attack based on speed and temper
    attack = np.round(effective_attack * ((speed + tuning.multiplier_adding_factor) / 100) * ((temper + tuning.multiplier_adding_factor) / 100))
    return max(0, attack),crit  # Ensure attack is non-negative

def estimate_battle(player_a_stats,player_b_stats):
    health_a = tuning.health_multiplying_factor * player_a_stats["Heart"]
    health_b = tuning.health_multiplying_factor * player_b_stats["Heart"]
    dps_a = ((tuning.base_dmg+player_a_stats["Strength"] - player_b_stats["Skin"])/tuning.base_attack_divisor+(player_a_stats["Head"]/tuning.special_skill_divisor)*player_a_stats["Special"]*tuning.special_scaling_factor)* ((player_a_stats["Speed"]  + tuning.multiplier_adding_factor) / 100) * ((player_a_stats["Temper"]  + tuning.multiplier_adding_factor) / 100)
    dps_b = ((tuning.base_dmg+player_b_stats["Strength"] - player_a_stats["Skin"])/tuning.base_attack_divisor+(player_b_stats["Head"]/tuning.special_skill_divisor)*player_b_stats["Special"]*tuning.special_scaling_factor)* ((player_b_stats["Speed"]  + tuning.multiplier_adding_factor) / 100) * ((player_b_stats["Temper"]  + tuning.multiplier_adding_factor) / 100)
    num_rounds_a = health_b/dps_a
    num_rounds_b = health_a/dps_b
    if(num_rounds_a>num_rounds_b):
        winner = "Player B"
    elif (num_rounds_b>num_rounds_a):
        winner = "Player A"
    else:
        winner = "Draw"
    
    return {
        "winner": winner,
        "num_rounds": num_rounds_a-num_rounds_b,
        "dps_a" : dps_a,
        "dps_b" : dps_b,
        "health_a" : health_a,
        "health_b":health_b
    }

def determine_winner_battle(player_a_stats, player_b_stats):
    """Simulate a battle between two players based on their stats."""
    # Initialize health
    health_a = tuning.health_multiplying_factor * player_a_stats["Heart"]
    health_b = tuning.health_multiplying_factor * player_b_stats["Heart"]
    round_number = 1
    while health_a > 0 and health_b > 0:
        print(f"Round {round_number}:")

        # Player A attacks Player B
        attack_a,crit_a = calculate_attack(
            strength=player_a_stats["Strength"],
            opposing_skin=player_b_stats["Skin"],
            speed=player_a_stats["Speed"],
            temper=player_a_stats["Temper"],
            special=player_a_stats["Special"],
            head=player_a_stats["Head"]
        )
        health_b -= attack_a


        # Player B attacks Player A
        attack_b,crit_b = calculate_attack(
            strength=player_b_stats["Strength"],
            opposing_skin=player_a_stats["Skin"],
            speed=player_b_stats["Speed"],
            temper=player_b_stats["Temper"],
            special=player_b_stats["Special"],
            head=player_b_stats["Head"]
        )
        health_a -= attack_b
        if(crit_a):
            print("Player A used their Special!")
        if(crit_b):
            print("Player B used their Special!")
        print(f"  Player A attacks with {attack_a:.2f} damage. Player B health: {health_b:.2f}")
        print(f"  Player B attacks with {attack_b:.2f} damage. Player A health: {health_a:.2f}")

        round_number += 1

    # Determine winner
    if health_a > 0:
        winner = "Player A"
        health = health_a
    elif health_b > 0:
        winner = "Player B"
        health = health_b
    else:
        # If tied, determine by least negative health
        if abs(health_a) < abs(health_b):
            winner = "Player A"
            health = health_a
        elif abs(health_b) < abs(health_a):
            winner = "Player B"
            health = health_b
        else:
            winner = "Draw"
            health = 0

    print("Battle Over!")
    print(f"Final Health: Player A: {health_a:.2f}, Player B: {health_b:.2f}")
    return {
        "winner": winner,
        "health":health
    }

