import pygame
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT

x1 = 750
x2 = 750
x3 = 740
x4 = 750
x5 = 770
x6 = 800
x7 = 830
x8 = 1000
x9 = 1030
x10 = 1200
x11 = 1230
y1 = 215
y2 = 265
y3 = 315
pygame.init()

WIDTH = 1000
HEIGHT = 1000
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables

circle_x = 0
circle_y = 0

# ---------------------------

running = True
while True:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False

    # GAME STATE UPDATES
    # All game math and comparisons happen here

    # DRAWING
    screen.fill((135, 206, 235))  # always the first drawing command

    pygame.draw.circle(screen, (255, 255, 0), (circle_x, circle_y), 150)
    circle_x += 1
    circle_y += 1
    if (circle_y >= 625):
      screen.fill((0, 0, 50))
      pygame.draw.circle(screen, (255, 255, 255), (0, 0), 150)
    # Must be the last two lines
    # of the game loop

    pygame.draw.rect(screen, (0, 255, 0), (0, 475, 9999, 2500))
    pygame.draw.rect(screen, (150, 75, 0), (65, 445, 15, 40))
    pygame.draw.circle(screen, (11, 150, 35), (75, 425), 30)
    pygame.draw.rect(screen, (150, 75, 0), (500, 445, 15, 40))
    pygame.draw.circle(screen, (11, 150, 35), (505, 425), 30)
    pygame.draw.rect(screen, (150, 75, 0), (650, 445, 15, 40))
    pygame.draw.circle(screen, (11, 150, 35), (655, 425), 30)
    pygame.draw.circle(screen, (50, 50, 50), (270, y1), 20)
    pygame.draw.circle(screen, (50, 50, 50), (270, y2), 20)
    pygame.draw.circle(screen, (50, 50, 50), (270, y3), 20)
    y1 -= 1
    y2 -= 1
    y3 -= 1
    pygame.draw.rect(screen, (170, 74, 68), (255, 215, 25, 100))
    pygame.draw.polygon(screen, (170, 74, 68), [(300, 225), (150, 350),
                                                (450, 350)])
    pygame.draw.rect(screen, (213, 184, 149), (175, 350, 250, 200))
    pygame.draw.rect(screen, (100, 50, 0), (250, 425, 60, 125))
    pygame.draw.circle(screen, (200, 200, 200), (300, 500), 5)
    pygame.draw.rect(screen, (100, 50, 0), (350, 375, 50, 50))
    pygame.draw.rect(screen, (135, 206, 235), (377, 403, 20, 20))
    pygame.draw.rect(screen, (135, 206, 235), (353, 403, 20, 20))
    pygame.draw.rect(screen, (135, 206, 235), (377, 378, 20, 20))
    pygame.draw.rect(screen, (135, 206, 235), (353, 378, 20, 20))
    pygame.draw.rect(screen, (0, 0, 0), (x1, 440, 30, 5))
    pygame.draw.rect(screen, (190, 190, 160), (x2, 445, 30, 30))
    pygame.draw.rect(screen, (200, 200, 200), (x3, 470, 50, 55))
    pygame.draw.rect(screen, (0, 0, 0), (x4, 525, 10, 45))
    pygame.draw.rect(screen, (0, 0, 0), (x5, 525, 10, 45))
    pygame.draw.circle(screen, (255, 255, 255), (
        x6,
        75,
    ), 25)
    pygame.draw.circle(screen, (255, 255, 255), (
        x7,
        75,
    ), 25)
    pygame.draw.circle(screen, (255, 255, 255), (
        x8,
        75,
    ), 25)
    pygame.draw.circle(screen, (255, 255, 255), (
        x9,
        75,
    ), 25)
    pygame.draw.circle(screen, (255, 255, 255), (
        x10,
        75,
    ), 25)
    pygame.draw.circle(screen, (255, 255, 255), (
        x11,
        75,
    ), 25)
    x6 -= 1
    x7 -= 1
    x8 -= 1
    x9 -= 1
    x10 -= 1
    x11 -= 1
    if (x1 > 265):
        x1 -= 1
        x2 -= 1
        x3 -= 1
        x4 -= 1
        x5 -= 1
    else:
        x1 += 999999999
        x2 += 999999999
        x3 += 999999999
        x4 += 999999999
        x5 += 999999999

    clock.tick(30)
    pygame.display.update()
