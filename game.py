import scoring
import deck_creator
import ai
import tuning
import numpy as np

def game_loop(player_a, player_b,scoring_arg,player_1,player_2):
    
    score_by_points = scoring_arg in ["points", "p"]
    """Main game loop."""
    for _ in range(7):  # Loop as long as there are cards to draw
        # Player A turn
        player_a.draw_card()
        if(player_1 in ["human", "h"]):
            print('-------------------------------\n------------------------------')
            print("Player A board: "+player_a.get_board())
            print("Player B board: "+player_b.get_board())
            print("You drew: \n"+player_a.get_hand())
            available_slots = [slot for slot, card in player_a.board.items() if card is None]
            while True:
            
                chosen_slot = input("Choose a slot to play your card: ").strip().capitalize()
                if chosen_slot not in available_slots:
                    if(chosen_slot=="Distribution"):
                        deck_creator.plot_stat_distributions()
                    else:
                        print("Invalid slot. Please choose again.")
                    continue

                variation = input("Choose a variation to play (1,2,3): ").strip()
                if variation not in player_a.hand["variations"]:
                    print("Invalid variation. Please choose again.")
                    continue
                break

        elif(player_1 in ["static_ai", "s"]):
            available_slots = [slot for slot, card in player_a.board.items() if card is None]
            chosen_slot,variation=ai.ai_choose_play(player_a.hand,available_slots,tuning.deck_stats)
        else:
            num_simulations =tuning.num_simulations
            chosen_slot,variation=ai.monte_carlo_ai(player_a,player_b,player_a.deck,score_by_points,num_simulations)    
        player_a.play_card(chosen_slot, variation)
        # Player B turn


        player_b.draw_card()
        if(player_2 in ["human", "h"]):
            print('-------------------------------\n------------------------------')
            print("Player A board: "+player_a.get_board())
            print("Player B board: "+player_b.get_board())
            print("You drew: \n"+player_b.get_hand())
            available_slots = [slot for slot, card in player_b.board.items() if card is None]
            while True:
            
                chosen_slot = input("Choose a slot to play your card: ").strip().capitalize()
                if chosen_slot not in available_slots:
                    if(chosen_slot=="Distribution"):
                        deck_creator.plot_stat_distributions()
                    else:
                        print("Invalid slot. Please choose again.")
                    continue

                variation = input("Choose a variation to play (1,2,3): ").strip()
                if variation not in player_b.hand["variations"]:
                    print("Invalid variation. Please choose again.")
                    continue
                break

        elif(player_2 in ["static_ai", "s"]):
            available_slots = [slot for slot, card in player_b.board.items() if card is None]
            chosen_slot,variation=ai.ai_choose_play(player_b.hand,available_slots,tuning.deck_stats)
        else:
            num_simulations =tuning.num_simulations
            chosen_slot,variation=ai.monte_carlo_ai(player_b,player_a,player_a.deck,score_by_points,num_simulations)    
        player_b.play_card(chosen_slot, variation)

    # Collect stats from the boards
    player_a_stats = {stat: card["stats"][stat] for stat, card in player_a.board.items() if card is not None}
    player_b_stats = {stat: card["stats"][stat] for stat, card in player_b.board.items() if card is not None}

    print("Board: ")
    print("player A: "+str(player_a_stats))
    print("player B: "+str(player_b_stats))

    # Determine winner
    if(score_by_points):
        result = scoring.determine_winner_scoring(player_a_stats, player_b_stats)
        print(f"Winner: {result['winner']}")
        print("Points per category:")
        print("Player A:")
        for category, points in result['player_a_points'].items():
            print(f"  {category}: {points:.2f}")

        print("Player B:")
        for category, points in result['player_b_points'].items():
            print(f"  {category}: {points:.2f}")

        print(f"Total A: {result['total_a']:.2f}")
        print(f"Total B: {result['total_b']:.2f}")
    else:
        result = scoring.estimate_battle(player_a_stats,player_b_stats)
        health_a = result["health_a"]
        health_b = result["health_b"]
        print("Health A: "+str(health_a)+ ", Health B: "+str(health_b))
        result = scoring.determine_winner_battle(player_a_stats, player_b_stats)
        print(f"Winner: {result['winner']}")




