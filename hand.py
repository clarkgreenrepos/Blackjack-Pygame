import pygame
from Button import Button

# Color for displaying cash
CASH_COL = (235, 201, 52)


class Hand:
    # Represents a Blackjack hand (player or house)
    def __init__(self, text_x, text_y, deck, card_type, start_x, start_y, cash):
        if card_type != "hand" and card_type != "house":
            raise ValueError("Hand card_type must be 'hand' or 'house'.")

        if cash < 1:
            self.cash = 1
        else:
            self.cash = cash

        self.card_type = card_type
        self.deck = deck

        self.text_x = text_x
        self.text_y = text_y

        self.start_x = start_x
        self.start_y = start_y

        self.cards = []
        self.total = 0
        self.ace_count = 0

        self.start_font = pygame.font.SysFont("yugothicuisemibold", 25)
        self.bust_font = pygame.font.SysFont("yugothicuisemibold", 80)
        self.hit_font = pygame.font.SysFont("yugothicuisemibold", 25)

    def add_card(self, surface):
        # Draw top card from deck, update total, handle aces
        top = self.deck.top_card()

        if top.get_type() == "ace":
            self.ace_count += 1

        self.cards.append(top)

        if self.card_type == "hand":
            self.deck.draw_top(surface, self.start_x + (len(self.cards) * 100), self.start_y)
        else:
            self.deck.draw_top(surface, self.start_x - (len(self.cards) * 100) - 50, self.start_y)

        new_card = self.cards[-1]

        if new_card.get_type() is None:
            self.total += new_card.value()
        else:
            self.total += self.ace_decision()

        if self.ace_count >= 1 and self.total > 21:
            self.total -= 10
            self.ace_count -= 1

        print_total = self.start_font.render(str(self.total), False, "green")
        pygame.draw.rect(surface, "black", (self.text_x, self.text_y, 40, 40), 0)
        surface.blit(print_total, (self.text_x, self.text_y))

    def button_input_hit(self):
        # Render "Hit" button and return True if mouse is over it
        hit = Button(None, (100, 500), "Hit", self.hit_font, "black", "yellow", "orange")
        screen = pygame.display.get_surface()
        hit.update(screen)
        if hit.checkForInput(pygame.mouse.get_pos()):
            return True
        return False

    def button_input_stand(self):
        # Render "Stand" button and return True if mouse is over it
        stand = Button(None, (100, 700), "Stand", self.hit_font, "black", "yellow", "orange")
        screen = pygame.display.get_surface()
        stand.update(screen)
        if stand.checkForInput(pygame.mouse.get_pos()):
            return True
        return False

    def ace_decision(self):
        # Decide value of ace as 11 or 1
        high = 11
        low = 1
        if self.total <= 10:
            return high
        else:
            return low

    def get_total(self):
        return self.total

    def get_cash(self):
        return self.cash

    def print_cash(self):
        # Draw current cash in top-left corner
        screen = pygame.display.get_surface()
        text = "$" + str(self.get_cash())
        img = self.start_font.render(text, True, CASH_COL)
        screen.blit(img, (0, 0))
        pygame.display.update()
