import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 800
SCREEN = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Complete Guide to PyGame Setup!")

CLOCK = pygame.time.Clock()

ICON = pygame.image.load("assets/icon.png")
pygame.display.set_icon(ICON)

BACKGROUND = pygame.image.load("assets/background.png")

FONT = pygame.font.SysFont("segoeuiblack", 64)
text = FONT.render("Hello, PyGame!", True, "white")
text_rect = text.get_rect(center=(WIDTH/2, 150))

pygame_image = pygame.transform.scale(pygame.image.load("assets/pygame.png"), (300, 119))
pygame_image_rect = pygame_image.get_rect(center=(WIDTH/2, 300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    SCREEN.blit(BACKGROUND, (0, 0))
    SCREEN.blit(text, text_rect)
    SCREEN.blit(pygame_image, pygame_image_rect)

    pygame.display.update()

    CLOCK.tick(60)