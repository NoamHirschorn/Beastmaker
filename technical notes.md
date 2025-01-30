## Technical/Game Balancing Notes

There are 2 immediate problems when trying to balance the game/create a scoring system. The first is to try to make a game where the best move is not always to just put the card best in one category in that slot. This just leads to a game with no real strategy and entirely dependent on luck. The second issue is the potential for one amazing card to simply overwhelm, so as long as a player does not put extremely weak cards in every other slot, one card will just have such relative advantage so as to be an insta win.

The points based scoring system is explicitly designed to deal with these two issues. The central premise is that points are scaled based on the relative margin between creatures in the category, but also on the absolute numbers. The idea is that even if a player has an extremely high stat in one category, as long as the opponent has a decent card opposing it, the number of points will be limited, and can be more than overcome if they play a weak card as well.  

**Example:**  
If player A has a 90 in Heart, even if player B only has a 70-75, player B can counter that by (depending on the exact settings), having a 55 in Special while player B only has a 45. The focus of the game is shifted much more on avoiding weak spots (and taking advantage of an opponent's), rather than relying on one strong card (solving the second problem).  

The first problem is also addressed as in the following example: Player A has Head and Temper still open, while player B has a strong card in Head and a medium card in Temper. If player A draws a card strong in Temper and slightly above average in Head, it still may make sense to play in Head, as the points from having a strong vs medium card in Temper will be more than outweighed by the potential to have a strong vs potentially weak card in Head, which can singlehandedly swing the game.  

The point of the game is thus shifted to trying to account for the variance of the last card(s) and to avoid being forced into putting a potentially weak card in a place where it would be devastating. The key variable (in the tuning file) is **'scaling_factor_strength'**, which determines how much emphasis should be put on this avoiding weak cards goal vs just trying to get a higher overall margin.

Additionally, it should be noted that different categories have different mean value and variance, so different categories feel different (see **deck_stats** in the tuning file). Higher means come with higher variance, so while it is possible to get extremely high numbers in some categories, since they are higher mean, the opponent also will likely have a relatively high value card, so the impact of the raw margin will be lessened.  

Also, as mentioned in the lore notes, **Strength and Skin oppose each other** (with the idea being offense vs defense), but otherwise all categories are opposed (i.e. margin is calculated between the values of each side in that category (e.g. **Player A's Heart - Player B's Heart**)).

---

## Battle Scoring System

The Battle scoring system was designed to be **more lore accurate** and less focused on balance/solving these problems. While the intention is for no 1 stat/card to be able to overwhelm/have too high an impact, this is less guaranteed, and there are therefore **many more tuning variables** to potentially fix any imbalances. 

The basic idea is that there still is a **Strength vs Skin** dynamic, subject to **modifiers of Temper and Speed**, while **Special** is a more powerful attack which happens less often.  

**Example of tuning:**  
In the default settings, **Special** might be a bit too weak (i.e. having a strong vs weak Special possibly does not impact the game as much as it should).  

**Potential solutions:**  
- Increasing the **special_scaling_factor** to make special attacks hit harder (based on the raw special stat).  
- Decreasing the **special_skill_divisor** to make Special moves hit more often (and thereby also buffing Strength).  
- Decreasing other factors such as **health_multiplying_factor**, which would lead to Special being more impactful from a relative sense.

---

## AI Behavior

The **Static AI** just attempts to use the strategy outlined by the first issue, simply seeing what percentile a card is for each category, and playing it in the "best" place for it.  

The **Monte Carlo AI** uses a **Monte Carlo search tree with an epsilon greedy strategy** to decide between exploring a random move or exploiting the Static AI strategy (which is taken to be a good heuristic).
