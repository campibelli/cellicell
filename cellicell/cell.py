import pygame
import random

# Colors
COLORS = {
    "blue": (0, 0, 255),
    "purple": (128, 0, 128),
    "white": (255, 255, 255),
    "green": (0, 255, 0)
}

# Change according to 'species'
CELL_RADIUS = 20
CELL_SPEED = 2
FONT = pygame.font.SysFont('Arial', 18)

class Cell:
    def __init__(self):
        self.x = random.randint(CELL_RADIUS, 800 - CELL_RADIUS)
        self.y = random.randint(CELL_RADIUS, 600 - CELL_RADIUS)
        self.color = random.choice(list(COLORS.values()))
        self.notation = random.choice(["+", "-"])
        self.dx = random.choice([-CELL_SPEED, CELL_SPEED])
        self.dy = random.choice([-CELL_SPEED, CELL_SPEED])

    def move(self):
        self.x += self.dx
        self.y += self.dy

        # Collision with wall!
        if self.x < CELL_RADIUS or self.x > 800 - CELL_RADIUS:
            self.dx = -self.dx
        if self.y < CELL_RADIUS or self.y > 600 - CELL_RADIUS:
            self.dy = -self.dy

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), CELL_RADIUS)
        text = FONT.render(self.notation, True, (0, 0, 0))
        text_rect = text.get_rect(center=(self.x, self.y))
        screen.blit(text, text_rect)