
import random

def create_deck():
    """Create a standard deck of 52 playing cards."""
    suits = ["C", "D", "H", "S"]  
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

def calculate_score(hand):
    """Calculate the score of a hand (considering Aces as 1 or 11)."""
    score = 0
    aces_count = 0

    # Loop through each card in the hand
    for card in hand:
        if card['rank'] in ['J', 'Q', 'K']:
            score += 10  # Face cards are worth 10
        elif card['rank'] == 'A':
            score += 11  # Aces are worth 11 initially
            aces_count += 1
        else:
            score += int(card['rank'])  # Numeric cards are worth their face value

    # Adjust for Aces: if score > 21, reduce Aces from 11 to 1
    while score > 21 and aces_count > 0:
        score -= 10  # Convert one Ace from 11 to 1
        aces_count -= 1

    return score