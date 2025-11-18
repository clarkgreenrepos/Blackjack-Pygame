import os
from random import shuffle
from card import Card


class Deck:
    # Represents a deck of cards loaded from Cards_new directory
    def __init__(self):
        self.card_list = []
        self.load_shuffle()

    def load_shuffle(self):
        # Load cards from folder, assign values, and shuffle
        self.card_list.clear()
        card_dir = "Cards_new"

        for filename in os.listdir(card_dir):
            card_type = None

            if filename.startswith("10") or filename.startswith("jack") or filename.startswith("king") or filename.startswith("queen"):
                value = 10
            elif filename.startswith("ace"):
                value = (11, 1)
                card_type = "ace"
            else:
                value = int(filename[0])

            new_card = Card(filename, card_type, value)
            self.card_list.append(new_card)

        shuffle(self.card_list)

    def pop_top(self):
        # Pop and return top card; reshuffle if empty
        if not self.card_list:
            self.load_shuffle()
        return self.card_list.pop(0)

    def draw_top(self, surface, x, y):
        # Draw top card at (x, y) and remove it from the deck
        self.pop_top().draw_card(surface, x, y)

    def top_card(self):
        # Return top card without removing; reshuffle if empty
        if not self.card_list:
            self.load_shuffle()
        return self.card_list[0]

    def reset(self):
        # Reload and reshuffle full deck
        self.load_shuffle()

    def length(self):
        # Number of cards remaining
        return len(self.card_list)
