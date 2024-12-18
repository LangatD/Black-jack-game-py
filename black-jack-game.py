import random
import time
import os  # Import the os module for clearing the terminal screen
from colorama import init, Fore, Back, Style

# Initialize colorama for colored text output
init(autoreset=True)

# Constants for suits, ranks, and values
suits = ("Spades ♠", "Clubs ♣", "Hearts ♥", "Diamonds ♦")
ranks = (
    "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A",
)
values = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, 
    "J": 10, "Q": 10, "K": 10, "A": 11,  # Aces initially count as 11
}

playing = True

# CLASS DEFINITIONS:

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ""  # start with an empty string
        for card in self.deck:
            deck_comp += "\n " + card.__str__()  # add each Card object's print string
        return "The deck has:" + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card


class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0  # start with zero value
        self.aces = 0  # add an attribute to keep track of aces

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == "A":
            self.aces += 1  # add to self.aces

    def adjust_for_ace(self):
        # Adjust for aces: if the hand's value is over 21, turn ace(s) from 11 to 1
        while self.value > 21 and self.aces:
            self.value -= 10  # turn an Ace from 11 to 1
            self.aces -= 1  # reduce the count of aces


# FUNCTION DEFINITIONS:

def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing

    while True:
        x = input("\nWould you like to Hit or Stand? Enter [h/s] ")

        if x[0].lower() == "h":
            hit(deck, hand)  # hit() function defined above

        elif x[0].lower() == "s":
            print("Player stands. Dealer is playing.")
            playing = False

        else:
            print("Sorry, Invalid Input. Please enter [h/s].")
            continue
        break


def show_some(player, dealer):
    print("\nPlayer's Hand:")
    for card in player.cards:
        print(f" {card}")
    print(f"Player's Hand Value = {player.value}")
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print(" " + str(dealer.cards[1]))  # Convert the card to a string before printing


def show_all(player, dealer):
    print("\nPlayer's Hand:")
    for card in player.cards:
        print(f" {card}")
    print(f"Player's Hand Value = {player.value}")
    print("\nDealer's Hand:")
    for card in dealer.cards:
        print(f" {card}")
    print(f"Dealer's Hand Value = {dealer.value}")


def player_busts(player, dealer):
    print("\n--- Player busts! ---")
    print("--- Dealer wins! ---")


def player_wins(player, dealer):
    print("\n--- Player wins! ---")


def dealer_busts(player, dealer):
    print("\n--- Dealer busts! Player wins! ---")


def dealer_wins(player, dealer):
    print("\n--- Dealer wins! ---")


def push(player, dealer):
    print("\nIt's a tie!")


# GAMEPLAY:
def print_colored():
    print("\n" + Fore.RED + Back.WHITE + "*"*64)  # Red text on white background
    print(Fore.GREEN + "                ♠♣♥♦ WELCOME TO BLACKJACK! ♠♣♥♦")
    print(Fore.YELLOW + "                          Let's Play!")
    print(Fore.RED + Back.WHITE + "*"*64)  # Red text on white background

def show_results(player, dealer):
    print("Player's Hand =", player.value)
    print("Dealer's Hand =", dealer.value)

def show_dealer_only(dealer):
    print("\nDealer's Hand:")
    print(*dealer.cards, sep="\n ")
    print("Dealer's Hand =", dealer.value)

def start_game():
    global playing
    print_colored()

    print(
        "Game Rules:  Get as close to 21 as you can without going over!\n\
        Dealer hits until he/she reaches 17.\n\
        Aces count as 1 or 11."
    )

    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # Show the cards:
    show_some(player_hand, dealer_hand)

    while playing:  # recall this variable from our hit_or_stand function

        # Prompt for Player to Hit or Stand
        hit_or_stand(deck, player_hand)
        show_some(player_hand, dealer_hand)

        if player_hand.value > 21:
            # Reveal the dealer's hidden card when the player busts
            print("\nDealer's Hand:", *dealer_hand.cards, sep="\n ")
            print(f"Dealer's Hand Value = {dealer_hand.value}")

            time.sleep(1)
            print("\n----------------------------------------------------------------")
            print("                     ★ Final Results ★")
            print("----------------------------------------------------------------")
            show_results(player_hand,dealer_hand)
            player_busts(player_hand, dealer_hand)
            time.sleep(1)
            print("\n----------------------------------------------------------------")
            print("                     ★ Final Results ★")
            print("----------------------------------------------------------------")

            show_results(player_hand, dealer_hand)
           #show_all(player_hand, dealer_hand)


            break

        # If the player chooses to stand, show results immediately
        if not playing:  # If the player has decided to stand, exit loop
            
            if player_hand.value <= 21:
                # Dealer's turn
                while dealer_hand.value < 17:
                    hit(deck, dealer_hand)
                    show_dealer_only(dealer_hand)

            

                # Test different winning scenarios
                time.sleep(1)
                print("\n----------------------------------------------------------------")
                print("                     ★ Final Results ★")
                print("----------------------------------------------------------------")
                show_results(player_hand, dealer_hand)

                if dealer_hand.value > 21:
                    dealer_busts(player_hand, dealer_hand)

                elif dealer_hand.value > player_hand.value:
                    dealer_wins(player_hand, dealer_hand)

                elif dealer_hand.value < player_hand.value:
                    player_wins(player_hand, dealer_hand)

                else:
                    push(player_hand, dealer_hand)
            break

def play_again():
    global playing
    new_game = input("\nPlay another hand? [Y/N] ")
    while new_game.lower() not in ["y", "n"]:
        new_game = input("Invalid Input. Please enter 'y' or 'n' ")
    
    if new_game[0].lower() == "y":
        os.system("cls" if os.name == "nt" else "clear")  # Clear the terminal screen (Windows/Unix)
        playing = True
        return True  # Return True to keep playing
    else:
        print("\n------------------------Thanks for playing!---------------------\n")
        return False  # Return False to stop the game


# Game entry point
if __name__ == "__main__":
    game_running = True
    while game_running:
        start_game()
        game_running = play_again()  # Continue playing if the player chooses 'y'
