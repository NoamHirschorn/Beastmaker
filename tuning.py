######Deck Creation #####

#(mean, variance) for each category when generate deck
#Higher mean with more variance, since punished more for lower values in points-scoring
#Otherwise, if someone gets a 70 in category with mean 40, can b difficult to overcome
deck_stats = {
        "Head": (45, 8),
        "Heart": (60, 14),
        "Temper": (45, 8),
        "Skin": (55, 12),
        "Speed": (50, 10),
        "Strength": (55, 12),
        "Special": (40, 6)
    }


######Points Scoring ######

#How much weight given in points scoring to emphasizing avoidance of low numbers vs margin
#Higher is less weight given to margin. Keep within range of 0.5 to 2.
scaling_factor_strength = 1.1

######Battle Scoring ######

#Base attack bonus when doing a battle (before scaling down). 
#Should be ~50-100 minimum to avoid 0 damage
base_dmg = 100
#How much jitter for the damage each attack does per turn in each direction
random_range = 5
#How much to scale the base attack down by
base_attack_divisor =4
#How often should use special attack (higher is less often).
#Should be at least 70-100 to guarantee less than 100% chance
special_skill_divisor = 200
#What percentage of Special stat is added to base attack to make effective attack
special_scaling_factor =.5
#For speed/temper (which give multiplier effects), how much boost them before calculating multiplier
multiplier_adding_factor = 50
#How much to scale Heart by to get base health
health_multiplying_factor = 4

###### Monte Carlo AI ######

#how many simulations the monte carlo ai should run per turn
num_simulations = 250
#how epsilon should range (higher means simulate more random moves)
epsilon_start = 0.7
epsilon_end = 0.1

###### General non-tuning stats

#maximum number of times a card can be in deck
max_appearances = 3
#minimum number
min_appearances = 1
#variations per card
variations_per_card=3
#number of cards in deck
total_appearances=100