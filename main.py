
# Import External Librarys
import pygame
import random


# Create walls,only run once
class Circles:
    def __init__(self, x, y, rad):
        self.x = x
        self.y = y
        self.rad = rad



def drawCircles():



# pygame setup
pygame.init()
screen = pygame.display.set_mode((720, 540))
clock = pygame.time.Clock()
running = True
dt = 0


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False





    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
