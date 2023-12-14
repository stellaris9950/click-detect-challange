
# Import External Librarys
import pygame
import random


# Create walls,only run once
class Circles:
    def __init__(self, radius: int, pos: pygame.Vector2, move: pygame.Vector2):
        self.radius = radius
        self.pos = pos
        self.move = move

    def moveCircle(self):
        self.pos += self.move
        if self.pos.x <= 0 or self.pos.x >= 720:
            self.move.x *= -1

        if self.pos.y <= 0 or self.pos.y >= 540:
            self.move.y *= -1

class Obstacles:
    def __init__(self, size: pygame.Vector2, pos: pygame.Vector2, move: pygame.Vector2):
        self.size = size
        self.pos = pos
        self.move = move

    def moveObstacles(self):
        self.pos += self.move
        if self.pos.x <= 0 or self.pos.x >= 720:
            self.move.x *= -1

        if self.pos.y <= 0 or self.pos.y >= 540:
            self.move.y *= -1


# pygame setup


circle_list = []
obstacles_list = []
def createDraw():

    times = random.randrange(5, 10)
    for i in range(times):
        circle_pos = pygame.Vector2(random.randrange(10, 700), random.randrange(10, 500))
        circle_direction = pygame.Vector2(5, 5)
        circle_created = Circles(20, circle_pos, circle_direction)

        circle_list.append(circle_created)

        square_size = pygame.Vector2(20, 20)
        square_pos = pygame.Vector2(random.randrange(10, 700), random.randrange(10, 500))
        square_direction = pygame.Vector2(5, 5)
        square_created = Obstacles(square_size, square_pos, square_direction)

        obstacles_list.append(square_created)


createDraw()

pygame.init()
screen = pygame.display.set_mode((720, 540))
clock = pygame.time.Clock()
running = True
dt = 0

circle_movement = 300*dt
boarders = []



while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")



    # move circle

    # x_moving = 300 * dt
    # y_moving = 300 * dt
    # for circles in circle_list:
    #     circles['x'] += x_moving
    #     circles['y'] += y_moving



    # draw
    for circle in circle_list:
        pygame.draw.circle(screen, "green", circle.pos, circle.radius)
        circle.moveCircle()
        # collisionDetection(position, circle_movement, boarders)

    for obstacle in obstacles_list:
        pygame.draw.rect(screen, "red", [obstacle.pos, obstacle.size])
        obstacle.moveObstacles()







    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
