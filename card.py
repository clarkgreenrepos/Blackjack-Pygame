import pygame
from os.path import join

# Default center position
half_resolution = WINDOW_WIDTH, WINDOW_HEIGHT = 1280 / 2, 720 / 2


class Card:
    # Represents a single card image and its value
    def __init__(self, img, card_type, num):
        self.img = img
        self.num = num
        self.card_type = card_type

        self.original_surface = pygame.image.load(join("Cards_new", self.img)).convert_alpha()
        self.card_surface = pygame.transform.scale(self.original_surface, (204.8, 281.6))
        self.card_rect = self.card_surface.get_frect(center=half_resolution)

    def value(self):
        # Return numeric value or tuple for ace
        return self.num

    def get_rect(self):
        return self.card_rect

    def set_rect(self, rect_center):
        # Set rect center to given (x, y)
        self.card_rect = self.card_surface.get_frect(center=rect_center)

    def get_surface(self):
        return self.card_surface

    def draw_card(self, surface, x, y):
        # Blit card image onto surface at (x, y)
        surface.blit(self.card_surface, (x, y))

    def get_type(self):
        # Return type: None or "ace"
        return self.card_type
