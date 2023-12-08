
# Import External Librarys
import pygame
import random


# Create walls,only run once
class Circles:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Wall:
    def __init__(self, x, y, length, width):
        self.length = length
        self.width = width
        self.x = x
        self.y = y
        self.collision_x = x + length
        self.collision_y = y + width



circle_list = []
# pygame setup



def createDrawCircles():

    times = random.randrange(5, 10)
    for i in range(times):
        x_of_c = random.randrange(10, 100)
        y_of_c = random.randrange(10, 100)

        circle_created = Circles(x_of_c, y_of_c)
        circle_list.append(vars(circle_created))

createDrawCircles()

def drawCircles(circle_list):
    for circle in circle_list:
        position = pygame.Vector2(circle['x'], circle['y'])
        pygame.draw.circle(screen, "green", position, 20)

def moveCircle(circle_list):

    x_moving = 300 * dt
    y_moving = 300 * dt

    for circles in circle_list:
        circles['x'] += x_moving
        circles['y'] += y_moving


def collisionDetection(screen_width, screen_height, circle_pos):
    boarders = []

    boarder = vars(Wall(0, 0, 10, screen_height))
    boarders.append(boarder)
    boarder = vars(Wall(0, 0, screen_width, 10))
    boarders.append(boarder)
    boarder = vars(Wall(screen_width - 10, 0, 10, screen_height))
    boarders.append(boarder)
    boarder = vars(Wall(0, screen_height - 10, screen_width, 10))
    boarders.append(boarder)


    # collision detection
    for boarder in boarders:

        if boarder['y'] - 30 <= circle_pos.y <= boarder['y'] - 30 + circle_movement and boarder['collision_x'] >= circle_pos.x >= \
                boarder['x'] - 30:
            circle_pos.y = boarder['y'] - 30
        if boarder["collision_y"] - circle_movement <= circle_pos.y <= boarder['collision_y'] and boarder[
            'collision_x'] >= circle_pos.x >= boarder['x'] - 30:
            circle_pos.y = boarder['collision_y']
        if boarder['x'] - 30 + circle_movement >= circle_pos.x >= boarder['x'] - 30 and boarder['collision_y'] >= circle_pos.y >= \
                boarder['y'] - 30:
            circle_pos.x = boarder['x'] - 30
        if boarder['collision_x'] >= circle_pos.x >= boarder['collision_x'] - circle_movement and boarder[
            'collision_y'] >= circle_pos.y >= boarder['y'] - 30:
            circle_pos.x = boarder['collision_x']


print(circle_list)


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

    moveCircle(circle_list)
    # draw
    drawCircles(circle_list)



    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
