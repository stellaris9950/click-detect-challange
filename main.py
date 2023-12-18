
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
    def __init__(self, rect: pygame.Rect, move: pygame.Vector2):
        self.rect = rect
        self.move = move

    def moveObstacles(self):
        self.rect.topleft += self.move
        if self.rect.left <= 0 or self.rect.left >= 720:
            self.move.x *= -1

        if self.rect.top <= 0 or self.rect.top >= 540:
            self.move.y *= -1


# pygame setup


circle_list = []
obstacles_list = []
def createDraw():

    times = random.randrange(5, 10)
    for i in range(times):
        circle_pos = pygame.Vector2(random.randrange(10, 700), random.randrange(10, 500))
        circle_direction = pygame.Vector2(2, 2)
        circle_created = Circles(20, circle_pos, circle_direction)

        circle_list.append(circle_created)

        # square_size = pygame.Vector2(20, 20)
        # square_pos = pygame.Vector2(random.randrange(10, 700), random.randrange(10, 500))
        rect_created = pygame.Rect(random.randrange(10, 700),
                                   random.randrange(10, 500),
                                   20, 20)
        square_direction = pygame.Vector2(5, 5)
        square_created = Obstacles(rect_created, square_direction)



        obstacles_list.append(square_created)




def mouseDetect(obstacle_list, circle_list):
    mouse_pos = pygame.mouse.get_pos()

    for obstacle in obstacles_list:
        if obstacle.rect.collidepoint(mouse_pos):
            return obstacle

    for circle in circle_list:
        if circle.pos.distance_to(mouse_pos) < circle.radius:
            return circle



createDraw()

pygame.init()

screen = pygame.display.set_mode((720, 540))
clock = pygame.time.Clock()
running = True
dt = 0

FONT = pygame.freetype.Font("Arial.ttf", 100)

circle_movement = 300*dt
boarders = []

lose = False
win = False

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            object_clicked = mouseDetect(obstacles_list, circle_list)
            if type(object_clicked) == Obstacles:
                obstacles_list.remove(object_clicked)
                lose = True
            elif type(object_clicked) == Circles:
                circle_list.remove(object_clicked)


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
        pygame.draw.rect(screen, "red", obstacle.rect)
        obstacle.moveObstacles()



    if lose:
        screen.fill("red")
        FONT.render_to(screen, (100, 150), "YOU LOSE", (50, 50, 50))

    if not circle_list:
        screen.fill("green")
        FONT.render_to(screen, (100, 150), "YOU WIN", (50, 50, 50))



    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
