def dealer_turn():
    global dealer_hidden, game_active

    if game_active:
        dealer_hidden = False
        while calculate_score(dealer_hand) < 17:
            dealer_hand.append(draw_card(deck))

        display_hands(player_hand, dealer_hand, dealer_hidden)

        player_score = calculate_score(player_hand)
        dealer_score = calculate_score(dealer_hand)

        if dealer_score > 21:
            print("\nDealer busts! You win!")
        elif dealer_score > player_score:
            print("\nDealer wins!")
        elif dealer_score < player_score:
            print("\nYou win!")
        else:
            print("\nIt's a tie!")

        game_active = False