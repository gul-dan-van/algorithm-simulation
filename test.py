import argparse
from ctypes.wintypes import POINT
import time
import random
import pygame

parser = argparse.ArgumentParser()
parser.add_argument('-r','--random',required=False)
parser.add_argument('-l','--length',required=False)
args = parser.parse_args()

class Points:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        

WIDTH, HEIGHT = 1500, 800
SCREEN = (WIDTH, HEIGHT)

FPS = 30
pygame.init()
pygame.display.set_caption("GIFT WRAPPING ALGO")
WIN = pygame.display.set_mode(SCREEN)
CLOCK = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (30, 30, 30)
GREY = (150, 150, 150)
BLUE = (0, 100, 255)
YELLOW = (255, 200, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

WIN.fill(BLACK)

POINT_NUMBER = (int(args.length) or 50)
OFFSET = 30
POINTS = []
CONVEX_HULL = []

if (args.random or '0') in '1TruetrueYesyes':
    # marking all points with white circles
    for n in range(POINT_NUMBER):
        point = Points(random.randint(OFFSET, WIDTH-OFFSET), random.randint(OFFSET, HEIGHT-OFFSET))
        pygame.draw.circle(WIN, BLUE, (point.x, point.y), 4)
        POINTS.append(point)
    pygame.display.update()
else:
    clicked = False
    run = True
    while run and len(POINTS)<POINT_NUMBER:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    run = False
                    break
            if not clicked and event.type == pygame.MOUSEBUTTONDOWN:
                pos = Points(*pygame.mouse.get_pos())
                clicked = True
                POINTS.append(pos)
                pygame.draw.circle(WIN, BLUE, (pos.x, pos.y), 4)
                pygame.display.update()
            if event.type == pygame.MOUSEBUTTONUP:
                clicked = False
    for n in range(len(POINTS), POINT_NUMBER):
        point = Points(random.randint(OFFSET, WIDTH-OFFSET), random.randint(OFFSET, HEIGHT-OFFSET))
        pygame.draw.circle(WIN, BLUE, (point.x, point.y), 4)
        POINTS.append(point)
    pygame.display.update()


# calling functions to perform program
JARVIS = JarvisMarch(POINTS, GREEN, WIN, RED, GREY, CONVEX_HULL)
JARVIS.left_most()
JARVIS.convex()

# joining all red dots (points that are part of hull) with blue lines
LEN = len(CONVEX_HULL)
for t in range(LEN):
    time.sleep(0.2)
    pygame.draw.line(WIN, BLUE, CONVEX_HULL[t], CONVEX_HULL[(t+1)%LEN], 5)
    pygame.display.update()

pygame.quit()
