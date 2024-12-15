def player_turn(deck, player_hand):
    """Handle the player's turn."""
    while True:
        display_hands("Your", player_hand)
        choice = input("Do you want to [H]it or [S]tand? ").strip().lower()
        if choice == 'h':
            new_card = deck.pop()
            print(f"You drew: {new_card}")
            player_hand.append(new_card)
            if calculate_score(player_hand) > 21:
                print_hand("Your", player_hand)
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
