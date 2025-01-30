import random
class Deck:
    def __init__(self, cards):
        """Initialize the deck with all card appearances."""
        self.cards = []
        for card in cards:  
            for _ in range(cards[card]["total_in_deck"]):
                self.cards.append(cards[card])

    def draw_card(self):
        """Draw a card from the deck and remove it."""
        if not self.cards:
            print("The deck is empty.")
            return None
        card = random.choice(self.cards)
        self.cards.remove(card)
        return card

class Player:
    def __init__(self, name, deck):
        """Initialize a player with a name, shared deck, and empty hand/board."""
        self.name = name
        self.deck = deck  # Reference to the shared deck
        self.hand = None  # A player can hold one card at a time
        self.board = {  # Each stat starts as empty
            "Head": None,
            "Heart": None,
            "Temper": None,
            "Skin": None,
            "Speed": None,
            "Strength": None,
            "Special": None
        }

    def draw_card(self):
        """Draw a card from the shared deck if the hand is empty."""
        if self.hand is not None:
            print(f"{self.name} already has a card in hand.")
            return
        
        self.hand = self.deck.draw_card()
        return

    def get_board(self):
        board_representation = []
        for stat, card in self.board.items():
            if card is None:
                board_representation.append(f"{stat}: Empty")
            else:
                board_representation.append(f"{stat}: {card['stats'][stat]}")
        return " | ".join(board_representation)
    def get_hand(self):
        if self.hand is None:
            return "No card in hand"

        hand_representation = []
        for variation_name, variation_data in self.hand["variations"].items():
            stats = variation_data["stats"]
            stats_str = ", ".join([f"{key}: {value}" for key, value in stats.items()])
            hand_representation.append(f"Variation {variation_name}: {variation_data['name']}: {stats_str}")

        return "\n".join(hand_representation)
     
    def play_card(self, stat, variation,print_results=True):
        """Play the card in hand in the specified variation for the given stat if it's empty."""
        if self.hand is None:
            print(f"{self.name} has no card in hand to play.")
            return

        if stat not in self.board:
            print(f"{stat} is not a valid board position.")
            return

        if self.board[stat] is not None:
            print(f"{stat} is already occupied on {self.name}'s board.")
            return

        if str(variation) not in self.hand["variations"]:
            print(f"Variation {variation} does not exist for this card.")
            return

        self.board[stat] = {
            "card_name": self.hand["name"],
            "variation": variation,
            "stats": self.hand["variations"][variation]["stats"]
        }
        if(print_results):
            print(f"{self.name} played {self.hand['variations'][variation]['name']} in {stat}.")
        self.hand = None  # Empty the hand after playing

    def display_board(self):
        """Display the current state of the player's board."""
        print(f"{self.name}'s Board:")
        for stat, card in self.board.items():
            if card is None:
                print(f"  {stat}: Empty")
            else:
                print(f"  {stat}: {card['card_name']} (Variation {card['variation']})")

