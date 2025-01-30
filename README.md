# Beastmaker Game Adaptation

This project adapts the Beastmaker game from Garth Nix's *Seventh Tower* series. Some changes were made from the 
source text, which are explained in the **lore notes** file. Meanwhile, notes about how the game was implemented and
the reasons for decisions made are in the **technical notes** file. No infringements intended.

---

## How to Run

To play a game:

1. **Download and unzip** the codebase.
2. **Open the command line interface** (cmd on Windows).
3. **Navigate to the folder** containing the files.
4. Run the game using:
   ```sh
   python run.py <scoring_system> <player_1> <player_2>
### `<scoring_system>`:
- `p` for **points-based scoring**
- `b` for **battle-based scoring**

### `<player_A>` & `<player_B>`:
- `s` for **Static AI**
- `m` for **Monte Carlo AI**
- `h` for **Human player**

#### **Example:**
```sh
python run.py p s h
```
This starts a game using **points-based scoring**, with a **Static AI** playing first and a **Human** playing second.

---

## How to Play

The game of **Beastmaker** involves two players playing cards in different categories to create a creature.  
In the book, the two creatures are simulated in battle, with the winner determining the game’s outcome.

### **Gameplay Overview**
- The game consists of multiple rounds.
- Each round, a player **draws a card** and chooses a slot (**category**) to place it in.
- Players alternate turns until **all 7 slots** on their board are filled:
  - **Head**, **Heart**, **Temper**, **Skin**, **Strength**, **Speed**, **Special**.
- Each card has **3 variations** (creature forms).
- A card can be played in **any open slot** using any variation (set once placed).
- The **variation’s stat** in the chosen category determines its effect.

### **Stat System**
- Stats are **binomially distributed** with different means and variances.
- Some stats (e.g., Heart) **tend to be higher** than others (e.g., Special).
- Strategic play is required—placing a **55 in Special** might be more valuable than a **65 in Heart**,  
  since all slots must be filled.

### **How to Play a Card**
1. **Enter the slot name** where you wish to place the card.
2. **Enter the variation number** to use for that slot.

To adjust mechanics, variables are available for tweaking in **tuning.py**.

---

## Creating a New Deck

To create a new deck, follow the initial steps from **How to Run**, but instead, run:
```sh
python create_deck.py
```
⚠️ **Warning:** Running this will remove all variation names.

---

## Scoring Systems

There are **two** scoring systems:

### **1. Points-Based Scoring (`p`)**
- Compares the final creatures' stats across all categories.
- Points are awarded based on the **difference** in stats between the creatures.
- The scoring considers both:
  - **Raw stat differences**
  - **The relative value of the stats** (e.g., a difference in Temper is weighted differently than Strength).
- For a detailed breakdown, refer to **technical notes** or the **code**.

### **2. Battle-Based Scoring (`b`)**
- Simulates a battle between the two creatures.
- The creatures fight until one is defeated.
- If both creatures are knocked out in the same round, the one with **less negative HP** wins.

---

## AI Opponents

There are two AI types available:

### **1. Static AI (`s`)**
- Plays cards based on the highest relative stat percentile in each category.

### **2. Monte Carlo AI (`m`)**
- Uses a **Monte Carlo Search Tree** to simulate possible outcomes before making a move.
- Generally stronger than Static AI but takes longer to compute.
- The AI’s computation time (which scales with skill) can be adjusted in **tuning.py**  
  using the `num_simulations` variable.

---

## File Descriptions

- **`ai.py`** – Functions for AI behavior and decision-making.
- **`classes.py`** – Structure for Deck and Player classes.
- **`create_deck.py`** – Wrapper for `deck_creator.py`.
- **`deck_creator.py`** – Functions to create a new deck and display its distribution.
- **`game.py`** – Central game loop.
- **`run.py`** – Wrapper for `game.py`.
- **`scoring.py`** – Defines game scoring functions.
- **`tuning.py`** – Contains hardcoded variables for game balance adjustments.

---

