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

def player_turn(deck, player_hand):
    
    while True:
        display_hands("Your", player_hand)
        choice = input("Do you want to [H]it or [S]tand? ").strip().lower()
        if choice == 'h':
            new_card = deck.pop()
            print(f"You drew: {new_card}")
            player_hand.append(new_card)
            if calculate_score(player_hand) > 21:
                display_hands("Your", player_hand)
                print("You busted! Dealer wins.\n")
                return False  # Player busted
        elif choice == 's':
            print("You stand.\n")
            return True  # Player chose to stand
        else:
            print("Invalid input. Please enter 'H' to Hit or 'S' to Stand.")


def main():
    """Main game loop."""
    print("Welcome to Blackjack!\n")

    while True:
        # Start a new game
        deck, player_hand, dealer_hand = start_game()

        # Player's turn
        if not player_turn(deck, player_hand):
            # Ask to play again if the player busted
            play_again = input("You busted! Do you want to play again? (yes/no): ").strip().lower()
            if play_again != 'yes':
                print("Thanks for playing!")
                break
            else:
                continue

        # Dealer's turn
        if not dealer_turn(deck, dealer_hand):
            # Ask to play again if the dealer busted
            play_again = input("Dealer busted! Do you want to play again? (yes/no): ").strip().lower()
            if play_again != 'yes':
                print("Thanks for playing!")
                break
            else:
                continue

        # Determine winner
        determine_winner(player_hand, dealer_hand)

        # Ask to play again
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
