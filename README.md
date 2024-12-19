# Blackjack Game

Welcome to the **Blackjack Game** project! This Python-based command-line game lets you play the classic casino game of Blackjack directly in your terminal. It's an engaging, interactive, and colorful way to experience the thrill of 21!

---

## Table of Contents

1. [About the Game](#about-the-game)
2. [Features](#features)
3. [Requirements](#requirements)
4. [Installation](#installation)
5. [How to Play](#how-to-play)
6. [File Structure](#file-structure)
7. [Gameplay Rules](#gameplay-rules)
8. [Future Enhancements](#future-enhancements)
9. [License](#license)

---

## About the Game

Blackjack (also known as 21) is a popular card game where the goal is to get as close to 21 as possible without exceeding it. In this implementation:

- You play against the dealer.
- The game handles card shuffling, dealing, and value adjustments for Aces dynamically.

This project is written entirely in Python and utilizes basic object-oriented programming (OOP) principles


## Features

- Interactive gameplay with user input.
- Realistic card shuffling and dealing.
- Automatic adjustments for Aces to prevent busting.
- Colorful terminal output using the `colorama` library.
- Clear and easy-to-read game interface.
- Replay option after each game round.

---

## Requirements

- **Python 3.6+**
-  **`colorama` library** for colored text output.


---

## Installation

1. Clone this repository or download the source code:

   ```bash
   git clone https://github.com/your-username/blackjack-game.git
   cd blackjack-game
2. nstall the required library:

  ```bash
  pip install colorama
3. Run the game:

  ```bash
    python blackjack.py
## How to Play
1. Start the game by running the script:

  ```bash
   python blackjack.py
  ```

2.  Follow the prompts:

   - Type `h` to **Hit** (draw a card).
   - Type s to **Stand** (end your turn).
3. Try to beat the dealer:

  - Get closer to 21 than the dealer without exceeding it.
  - If your hand's value exceeds 21, you bust and lose the round.
  - After the game ends, choose whether to play again.

## File Structure
```
blackjack/
├── __pycache__/      # Compiled Python files 
├── art.py            # Contains game visuals 
├── black-jack-game.py  # Main game script
├── Pipfile           # Dependencies managed with Pipenv
├── Pipfile.lock      # Locked dependency versions
└── README.md         # Project documentation
```
## Gameplay Rules
1. The dealer and the player are each dealt two cards. The dealer hides one card.
2. The player chooses to either:
 - **Hit:** Draw an additional card.
 - **Stand:** End their turn.
3. The dealer reveals their hidden card and continues to draw until their hand's value is 17 or higher.
4. The winner is determined as follows:
   - If the player exceeds 21, they lose (bust).
   - If the dealer exceeds 21, the player wins.
   - If both stay under 21, the higher hand value wins.
   - A tie results in a push (no winner).
     
## Future Enhancements
- Add betting functionality with virtual currency.
- Support for multiple players.
- Create a graphical user interface (GUI) version.
- Implement save and load game history features.

## License
This project is licensed under the MIT License. 
