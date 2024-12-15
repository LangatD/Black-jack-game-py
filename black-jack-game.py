
import random

def create_deck():
    """Create a standard deck of 52 playing cards."""
    suits = ["C", "D", "H", "S"]  # Clubs, Diamonds, Hearts, Spades
    values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    return [{"rank": value, "suit": suit} for suit in suits for value in values]

def shuffle_deck(deck):
    """Shuffle the deck of cards in place."""
    random.shuffle(deck)

def draw_card(deck):
    """Draw a card from the deck."""
    if len(deck) == 0:
        return None
    return deck.pop()