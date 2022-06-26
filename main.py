import time
from random import randint
import pygame
from pygame.locals import *
from random import *
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-l", "--length", required=False)
parser.add_argument("-sw", "--screen_width", required=False)
parser.add_argument("-sh", "--screen_height", required=False)
args = parser.parse_args()

pygame.init()

clock = pygame.time.Clock()

screen_width = args.screen_width or 1000
screen_height = args.screen_height or 500
option_width, option_height = 160, 40

RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
YELLOW = (240, 240, 0)
BLUE = (0, 0, 255)
GREY = (150, 150, 150)
DGREY = (30, 30, 30)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
PINK = (204, 51, 139)

INF = int(1e9)

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sorting")


def draw_text(text, font, font_size, text_col, x, y):
    FONT = pygame.font.SysFont(font, font_size)
    img = FONT.render(text, True, text_col)
    _, _, w, h = img.get_rect()
    w //= 2
    h //= 2
    screen.blit(img, (x - w, y - h))


class Button:
    def __init__(self, text, x, y, color=WHITE):
        self.text = text
        self.width = option_width
        self.height = option_height
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.color = color

    def render(self):
        pygame.draw.rect(screen, self.color, self.rect, width=2)
        draw_text(self.text, "kokila", 30, WHITE, *self.rect.center)


def draw_bg():
    screen.fill(BLACK)


def selection_sort(length=100):
    fps = length // 10
    random_list = choices(range(1, length ** 2), k=length)
    max_number = max(random_list)
    block_width = screen_width / length
    run = True
    for i in range(length - 1):

        clock.tick(fps)
        if not run:
            break
        k = i
        mn = random_list[i]
        for j in range(i + 1, length):
            if not run:
                break
            if mn > random_list[j]:
                k = j
                mn = random_list[j]

            def draw(i, k, j):
                screen.fill(DGREY)
                pygame.draw.line(screen, WHITE, (0, 80), (screen_width, 80))
                draw_text("Selection Sort", "impact", 60, WHITE, screen_width // 2, 40)

                for x in range(length):
                    if x == i or x == k:
                        color = BLUE
                        if x == j:
                            color = RED
                    elif x == j:
                        color = RED
                    else:
                        color = WHITE

                    if INF in [i, k, j]:
                        color = WHITE

                    block_height = random_list[x] * (screen_height - 100) // max_number
                    pygame.draw.rect(
                        screen,
                        color,
                        (
                            x * block_width,
                            screen_height - block_height,
                            block_width,
                            block_height,
                        ),
                        0,
                    )

            for event in pygame.event.get():
                if event.type == QUIT:
                    run = False
                    return

            draw(i, k, j)
            pygame.display.update()

        random_list[i], random_list[k] = random_list[k], random_list[i]

    time.sleep(2)


def merge_sort(length):
    fps = length // 10
    random_list = choices(range(1, length ** 2), k=length)
    max_number = max(random_list)
    block_width = screen_width / length
    merge_sort.run = True

    def draw(k, i, j):
        screen.fill(DGREY)
        pygame.draw.line(screen, WHITE, (0, 80), (screen_width, 80))
        draw_text("Merge Sort", "impact", 60, WHITE, screen_width // 2, 40)

        for x in range(length):
            if x == i or x == j:
                color = RED
            elif x == k:
                color = BLUE
            else:
                color = WHITE

            if INF in [i, k, j]:
                color = WHITE

            block_height = random_list[x] * (screen_height - 100) // max_number
            pygame.draw.rect(
                screen,
                color,
                (
                    x * block_width,
                    screen_height - block_height,
                    block_width,
                    block_height,
                ),
                0,
            )

        pygame.display.update()

    def sort(l, r):
        if not merge_sort.run:
            return

        for event in pygame.event.get():
            if event.type == QUIT:
                merge_sort.run = False
                return

        n = r - l + 1
        if n == 2:
            clock.tick(fps)
            draw(-1, l, r)
            if random_list[l] > random_list[r]:
                random_list[l], random_list[r] = random_list[r], random_list[l]
            draw(-1, l, r)

            return

        if n < 2:
            draw(-1, l, l)
            return

        sort(l, l + n // 2 - 1)
        sort(l + n // 2, r)

        i = 0
        j = 0

        clock.tick(fps)
        while i < n // 2 and j < (n + 1) // 2:
            for event in pygame.event.get():
                if event.type == QUIT:
                    merge_sort.run = False
                    return
            if not merge_sort.run:
                return

            clock.tick(fps)
            draw(max(l, l + i + j - 1), l + i + j, l + n // 2 + j)
            if random_list[l + i + j] < random_list[l + n // 2 + j]:
                i += 1
            else:
                temp_list = (
                    random_list[l : l + i + j]
                    + [random_list[l + n // 2 + j]]
                    + random_list[l + i + j : l + n // 2 + j]
                    + random_list[l + n // 2 + j + 1 : r + 1]
                )
                random_list[l : r + 1] = temp_list
                j += 1

            draw(max(l, l + i + j - 1), l + i + j, l + n // 2 + j)

    sort(0, length - 1)
    time.sleep(2)


def JarvisMarch(length):
    screen.fill(DGREY)
    pygame.draw.line(screen, WHITE, (0, 80), (screen_width, 80))
    draw_text("Jarvis March", "impact", 60, WHITE, screen_width // 2, 40)

    class Points:
        def __init__(self, x, y):
            self.x = x
            self.y = y
            

    class JarvisMarch:
        def __init__(self, points, green, screen, red, grey, convex_hull):
            self.points = points
            self.green = green
            self.screen = screen
            self.red = red
            self.grey = grey
            self.convex_hull = convex_hull

        # Find leftmost point among the given points
        def left_most(self):

            leftmost = 0
            
            for i in range(1, len(self.points)):
                if self.points[i].x < self.points[leftmost].x:
                    leftmost = i

            pygame.draw.circle(self.screen, self.green, (self.points[leftmost].x, self.points[leftmost].y), 7, 1)
            pygame.display.update()

            return leftmost
        
        # function to determine the magnitude of angle subtended by 3 specific points
        def orientation(self, a, b, c):

            # variable to store cross product
            cross_products = (b.y - a.y) * (c.x - b.x) - (b.x - a.x) * (c.y -  b.y)
            
            # if cross procut will be negative, that would mean that this point along with previous point that was part of hull will subtend an angle
            # on any other point in direction opposite to angle subtended by previous point and any other point on the current point
            if cross_products < 0:
                return 1
            else:
                return 0

        # funtion to highlight outermost points
        def convex(self):
            length = len(self.points)

            # if number of points is less than 3, that would mean forming a polygon will not be possible
            if length < 3:
                return
            
            current_point = self.left_most()

            # list to store outermost points
            hull = []

            # starting with leftmost point
            a = current_point
            b = 0
            running = True
            while running:

                # 'a' will be the point that should be included in hull
                hull.append(a)

                # checking for points just after a
                b = (a + 1) % length
                time.sleep(0.1)
                
                # checking whether 'b' makes obtuse angle with 'a' and other poitns
                for i in range(length):
                    pygame.draw.line(self.screen, self.grey, (self.points[a].x, self.points[a].y), (self.points[i].x, self.points[i].y), 1)
                    pygame.display.update()

                    # checking for convex angle condition
                    if(self.orientation(self.points[a], self.points[i], self.points[b]) == 1):
                        b = i
                a = b

                # we'll have to stop the loop if we will come back to original point after circling around
                if a == current_point:
                    running = False
            
            # highlighting all points that are part of hull with red circles
            for n in hull:
                pygame.draw.circle(self.screen, self.red, (self.points[n].x, self.points[n].y), 8, 3)
                pygame.display.update()
                self.convex_hull.append((self.points[n].x, self.points[n].y))
                time.sleep(0.05)

    fps = 30
    OFFSET = 30
    POINTS = []
    CONVEX_HULL = []
    
    clicked = False
    run = True
    while run and len(POINTS)<length:
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
                pygame.draw.circle(screen, BLUE, (pos.x, pos.y), 4, 1)
                pygame.display.update()
            if event.type == pygame.MOUSEBUTTONUP:
                clicked = False
    for n in range(len(POINTS), length):
        point = Points(randint(OFFSET, screen_width-OFFSET), randint(OFFSET, screen_height-OFFSET))
        pygame.draw.circle(screen, BLUE, (point.x, point.y), 4, 1)
        POINTS.append(point)
    pygame.display.update()

    # calling functions to perform program
    JARVIS = JarvisMarch(POINTS, GREEN, screen, RED, GREY, CONVEX_HULL)
    JARVIS.left_most()
    JARVIS.convex()

    # joining all red dots (points that are part of hull) with blue lines
    LEN = len(CONVEX_HULL)
    for t in range(LEN):
        time.sleep(0.2)
        pygame.draw.line(screen, PINK, CONVEX_HULL[t], CONVEX_HULL[(t+1)%LEN], 3)
        pygame.display.update()

    time.sleep(2)


functions = {
    "Selection Sort": selection_sort,
    "Merge Sort": merge_sort,
    "Jarvis March": JarvisMarch
     }


def menu():
    options = list(functions.keys())

    option_left = (screen_width - option_width) // 2
    block_height = len(options) * option_height
    options_height = [
        h
        for h in range(
            (screen_height - block_height) // 2,
            (screen_height + block_height) // 2 + option_height,
            option_height,
        )
    ]
    options_button = [
        Button(options[i], option_left, options_height[i]) for i in range(len(options))
    ]

    run = True
    clicked = False
    pos = None
    while run:

        clock.tick(60)
        draw_bg()

        for button in options_button:
            button.render()

            if clicked and button.rect.collidepoint(clicked_pos):
                functions[button.text](max(10, int(args.length or 100)))
                clicked = False

        for event in pygame.event.get():
            if event.type == QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONUP:
                clicked = False
            if clicked == False and event.type == pygame.MOUSEBUTTONDOWN:
                clicked_pos = pygame.mouse.get_pos()
                clicked = True

        pygame.display.update()


menu()

pygame.quit()
