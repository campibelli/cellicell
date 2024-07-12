import pygame
from cell import Cell

#Init
pygame.init()

#Scr size
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("cellicell :D")

# List of cells
cells = [Cell() for _ in range(10)]

#gameloop (check fps and stuff later)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #moving, spawn
    screen.fill((0, 0, 0))
    for cell in cells:
        cell.move()
        cell.draw(screen)

    pygame.display.flip()
    pygame.time.delay(30)

pygame.quit()