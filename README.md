# Blackjack – Pygame Implementation

A simple, fully playable Blackjack game built with Python and Pygame.  
Includes a player hand, dealer (house) hand, hit/stand buttons, card graphics, ace logic, and a basic betting system.

The code is fully modular, with each class placed in its own file.

## Features

- Full Blackjack gameplay loop  
- Player and dealer hands with automatic scoring  
- Accurate Ace logic (counts as 11 or 1 depending on total)  
- Hit / Stand buttons with hover detection  
- Card images loaded from the Cards_new directory  
- Player cash system (win = double, lose = half)  
- Automatic deck reshuffling  
- Modular class layout (Hand, Deck, Card, Button)

## Project Structure

Blackjack/  
    main.py        – Main game loop, menu, drawing  
    hand.py        – Player/Dealer hand logic, buttons  
    house.py       – Deck loading/shuffling/drawing  
    card.py        – Card image + value handling  
    Button.py      – Reusable UI button class  
    card_sprites/     – Directory containing card images (PNG)  

## Requirements

- Python 3.10+  
- Pygame installed  
- A folder named `Cards_new` with all card images  

Install Pygame:

pip install pygame

## How to Run

python main.py

## Controls

- Hit — Draw a new card  
- Stand — End player's turn and let the dealer draw  
- Close window — Quit game  

## Notes

- All card graphics must be placed inside the `Cards_new` folder.  
- The deck automatically reshuffles when empty.  
- Cash cannot drop below 1.  
- Player and dealer totals update in real-time as cards are drawn.

## License

This project is free to use and modify.
