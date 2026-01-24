import pygame
from house import Deck
from hand import Hand

pygame.init()

# Window / display setup
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Blackjack")
clock = pygame.time.Clock()

# Fonts
blackjack_font = pygame.font.SysFont("yugothicuisemibold", 40)
start_font = pygame.font.SysFont("yugothicuisemibold", 25)
outcome_font = pygame.font.SysFont("yugothicuisemibold", 70)
bust_font = pygame.font.SysFont("yugothicuisemibold", 80)

# Colors
TEXT_COL = (255, 255, 255)
LOSE_COL = (255, 0, 43)
WIN_COL = (0, 255, 47)
PUSH_COL = (249, 255, 79)

# Simple background (replace with table image if you have one)
bg = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
bg.fill((0,0,0))

# Shared deck
deck = Deck()


def draw_text(text, font, text_col, x, y):
    # Draw text at (x, y) on the main display surface
    img = font.render(text, True, text_col)
    display_surface.blit(img, (x, y))

def player_win(money):
    draw_text("YOU WIN", outcome_font, WIN_COL, WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 - 20)
    player_cash = money * 2
    pygame.display.update()
    pygame.time.wait(3000)
    game_loop(player_cash)

def player_lose(money):
    draw_text("YOU LOSE", outcome_font, LOSE_COL, WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 - 20)
    player_cash = money / 2
    pygame.display.update()
    pygame.time.wait(3000)
    game_loop(int(player_cash))


def game_loop(player_cash):
    if player_cash < 1:
        player_cash = 1
    print(player_cash)
    # Main game loop for one round of Blackjack
    display_surface.blit(bg, (0, 0))

    # Create house (dealer) hand
    house_hand = Hand(WINDOW_WIDTH - 100, WINDOW_HEIGHT - 600, deck, "house", WINDOW_WIDTH - 200, 0, 0)

    # Create player hand
    player_hand = Hand(100, 600, deck, "hand", WINDOW_WIDTH / 2 - 500, WINDOW_HEIGHT - 281.6, player_cash)

    player_hand.print_cash()

    running = True

    # Initial deal: 1 card to house, 2 to player
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        house_hand.add_card(display_surface)
        for _ in range(2):
            player_hand.add_card(display_surface)

        pygame.display.update()
        break

    # Player turn: hit / stand
    while running:
        hit_button = player_hand.button_input_hit()
        stand_button = player_hand.button_input_stand()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            # Check for natural blackjack
            if player_hand.get_total() == 21:
                display_bj = bust_font.render("BLACKJACK!", False, "blue")
                player_cash *= 2
                display_surface.blit(display_bj, (WINDOW_WIDTH / 2 + 100, WINDOW_HEIGHT / 2 - 50))
                pygame.display.update()
                pygame.time.wait(3000)
                game_loop(player_cash)
                return

            # Hit logic
            if hit_button and event.type == pygame.MOUSEBUTTONUP:
                player_hand.add_card(display_surface)

                if player_hand.get_total() > 21:
                    display_bust = bust_font.render("BUST!", False, "red")
                    player_cash = player_cash / 2
                    display_surface.blit(display_bust, (WINDOW_WIDTH / 2 + 100, WINDOW_HEIGHT / 2 - 50))
                    pygame.display.update()
                    pygame.time.wait(3000)
                    game_loop(int(player_cash))
                    return

            # Stand logic
            if stand_button and event.type == pygame.MOUSEBUTTONUP:
                while running:
                    if house_hand.total <= 21:
                        if house_hand.total == player_hand.total:
                            draw_text("PUSH", outcome_font, PUSH_COL, WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 - 20)
                            pygame.display.update()
                            pygame.time.wait(3000)
                            game_loop(int(player_cash))
                            return
                        if house_hand.total > player_hand.total:
                            player_lose(player_cash)
                            return
                        if house_hand.total >= 17:
                            if house_hand.total < player_hand.total:
                                if house_hand.total > player_hand.total:
                                    player_lose(player_cash)
                                    return
                            else:
                                player_win(player_cash)
                                return

                    else:
                        player_win(player_cash)
                        return
                    
                    house_hand.add_card(display_surface)
                    pygame.display.update()
                    pygame.time.wait(1000)

        pygame.display.update()
        clock.tick(60)


def main_menu():
    # Simple main menu: press SPACE to start
    while True:
        display_surface.fill("black")
        draw_text("Blackjack", blackjack_font, TEXT_COL, 300, 100)
        draw_text("Press SPACE to start", start_font, TEXT_COL, 300, 150)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    display_surface.fill("black")
                    pygame.display.update()
                    game_loop(1)

        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main_menu()
