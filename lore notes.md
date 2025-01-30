## Lore Adaptation Notes

### **1) No Switching Variations**
The books do not seem to specify if there are subtypes within each slot  
(i.e. different types of strength, ability to set traps vs find opponent weak points for head, etc).  
Instead, it basically just seems to involve playing cards that are good for each slot (without these tradeoffs).  

Therefore, once a card is played in a slot, since they also cannot move slots,  
one variation will be strictly as good/better than the others.  
Thus, the **switching of variations does not actually serve a helpful purpose**.  

Moreover, there is a slight incentive for each player to switch variations as much as allowed  
in the hopes of their opponent playing an additional card,  
giving them more information committing their cards, which simply wastes time  
as neither player has any reason to do this.  

Finally, there is no game advantage to keeping this mechanic  
since it's not as though additional cards are drawn or anything to give more options for the player.  
Therefore, **this mechanic was simply removed**, and a card can just be played at any variation.  

In the text, there is some **ambiguity** over whether the last card can switch variations  
(it discusses playing the final card locking the others in,  
but does this mean there is time before locking in the last card to change its variations?).  
Playing it in a different variation was allowed, as much of the game already is about managing  
the variance of the last card(s) drawn, which would become even more extreme  
if only the first variation was allowed. This would lead to a **complete lack of choice**  
for the last slot, contrary to how the books make it feel,  
as well as exacerbating problems with gameplay.

---

### **2) Variations Being Better Than Others**
Since the game uses **explicit numbers**, it is easy to see that each card  
has a best variation per stat.  

Indeed, the **AI just uses the max value per stat** when considering each card.  
Nevertheless, out of respect to the lore, **all 3 variations are shown** on the card,  
and the player must specify which variation to use.

---

### **3) Scoring**
The game scores itself by **simulating the two creatures and having them fight**.  
This is obviously impractical on anything other than a **dedicated modeling/fighting simulation**,  
and is well beyond the scope of the project.  

Even more so, a truly **faithful adaptation** would require creating  
a unique special ability for each creature and weaving it into gameplay.  

Therefore, **two different scoring systems were created**:
1. **Points-Based Scoring**  
   - Judges how the creatures compare across different categories.  
   - More competitive (see technical notes), but less **lore accurate**.  
2. **Battle-Based Scoring**  
   - Meant to feel **more accurate to the books**.  

However, this leads to the next point about **categories**.

---

### **3a) Categories**
The books do not go into detail about **how the different categories interact/functions served**.  

For example:
- **What is the benefit of a good vs medium vs bad Temper?**  
  - Does it mean the creature is cowardly and runs away?  
  - But they are already fighting, and **Heart is responsible for not giving up**.  
- **Does Strength determine which animal is stronger in a fight?**  
  - Like two bucks locking antlers?  
  - Or does it refer to **sharpness and the ability to break the opponent’s skin**?  

The **battle simulator** used these interpretations:

- **Heart:** Corresponds to how determined/long a creature will fight (**Health**).  
- **Skin:** How tough a creature’s skin is (**Defense Stat**).  
- **Strength:** The counterpart to Skin, essentially a base **Offense Stat**.  
  - Based on the fights in the book, it was imagined that fights would be more about **slashing**  
    rather than blunt force, so Strength should oppose Skin rather than two creatures’ Strength opposing each other.  
- **Temper:** How aggressive a creature is (**Rage modifier** that increases attack power).  
- **Speed:** How fast a creature is, determining how many attacks it can do.  
  - Although battles are divided into rounds for ease of tracking,  
    the idea is that Speed **increases damage per second**,  
    making it an **attack modifier**.  
  - *(Note: Theoretically, Speed could also increase dodge/evasion,  
    but this risked making it too overbearing.)*  
- **Special:**  
  - In theory, Special **should not be a number system at all**,  
    and should overturn the entire structure of the fight.  
  - Even if not taken to that extreme, it could **modify health, defense, or offense**  
    in various ways.  
  - However, **having Special not be a simple 1-100 scale**  
    would make it much more difficult to create an AI for.  
  - The basic nature of the combat system means there is not much room  
    for each creature to have its own unique special ability.  
  - **Practical Decision:**  
    - Special was simplified as a **form of surprise extra damage**,  
      making it at least **feel bursty and special**,  
      even if in a very different way than is described in the book.  
- **Head:** How smart the creature is.  
  - Could be interpreted as **finding weak spots, setting traps, etc.**  
  - Instead, it was paired with Special to **balance out the “critical hit” nature of the mechanic**.  
  - The idea is that **smarter creatures can more often maneuver battles**  
    to bring their Special ability into play.

---

### **3b) Interaction**
The book says that much of the point of the game is to **trick your opponent regarding what type of creature you are making**.  
However, it does not explain **how this is done or what effect it might have**.  

This might imply **subcategories** as suggested in point **1**, but even if so,  
there is still **no elaboration of what they might be or how they would interact**.  

Therefore, they were **not included in the game**.  

As a consequence:
- The **points system does encourage some adjustment of play**  
  based on the opponent’s board.  
- However, the overall **interaction level** between players  
  when creature-building is **markedly less than the feeling conveyed in the text**.

---

### **4) Cards in the Deck**
The books specify that the **deck contains 100 cards**  
but also shows that **multiple copies of a card can exist**.  

However, **there are no hints** about:
- The **frequency of common vs uncommon cards**.  
- Whether, as with many card games, **stronger cards are less frequent**.  

To balance this:
- A **maximum of 3 of the same card per deck** was set  
  to ensure sufficient variety while avoiding situations  
  where the same card is played repeatedly.  
- This avoids **both players using the same card too often**,  
  which appeared to happen in the book’s game.  
- It is implied that **each creature is only ever paired with others in a set**,  
  meaning they were **in fact the same card**.  

Additionally:
- A system was created so that **the more extreme the stats on a card**,  
  the **less frequently it appears** in the deck, making these cards feel **more unique**.  

Another aspect **not specified** is whether the deck is:
- **Standardized like a draft cube**,  
- Or **just a pile of 100 valid cards**.  

The books mention that a certain card is **rarely seen**,  
but is that because:
1. It is **one card in a game that is rarely played**,  
   and only **14/100 cards are played per game**?  
2. Or because **the card is rare and not even in most decks**?  

For **simplicity’s sake**, the assumption was made  
that there is a **standardized deck**.

---

### **5) Card Names**
Just to be on the **safe side**, even though this is just  
a **non-monetized passion project**, **no names from the book** have been copied or used.
