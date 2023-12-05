
# Import External Librarys
import pygame
import random


# Create walls,only run once
class Circles:
    def __init__(self, x, y):
        self.x = x
        self.y = y




circle_list = []


def createDrawCircles():

    times = random.randrange(5, 10)
    for i in range(times):
        x_of_c = random.randrange(10, 100)
        y_of_c = random.randrange(10, 100)

        circle_created = Circles(x_of_c, y_of_c)
        circle_list.append(vars(circle_created))


def drawCircles(circle_list):
    for circle in circle_list:
        pygame.draw.circle(screen, "green", circle['x_of_c'], circle['y_of_c'], 10)

createDrawCircles()
print(circle_list)

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
