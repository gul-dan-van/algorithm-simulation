import pygame
from pygame.locals import *
from random import *

pygame.init()

clock=pygame.time.Clock()

screen_width=1000
screen_height=500

RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255,255,255)
YELLOW = (240,240,0)
BLUE=(0,0,255)
GREEN=(0,255,0)
BLACK=(0,0,0)

INF=int(1e9)

screen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Selection Sort')


length=20
numbers=sample(range(100),length)
# numbers=[*range(20,0,-1)]
max_number=max(numbers)
fps=length//10
# fps=60

block_width=screen_width/length

def draw(i,k,j):
    screen.fill(BLACK)
    pygame.draw.line(screen,WHITE,(0,80),(screen_width,80))

    for x in range(length):
        if x==i or x==k:
            color=BLUE
            if x==j:
                color=RED
        elif x==j:
            color=RED
        else:
            color=WHITE

        if INF in [i,k,j]:
            color=WHITE

        block_height = numbers[x]*(screen_height-100)//max_number
        pygame.draw.rect(screen,color,( x*block_width, screen_height-block_height, block_width, block_height),0)
        # pygame.draw.rect(screen,BLACK,( x*block_width, screen_height-block_height, block_width, block_height),1)


run=True
i=0
prev=pygame.time.get_ticks()
while run:
    clock.tick(fps)
    
    for event in pygame.event.get():
        if event.type==QUIT:
            run=False

    if i<length:

        m=numbers[i]
        k=i
        for j in range(i+1,length):

            if numbers[j]<numbers[k]:
                m=numbers[j]
                k=j

            for event in pygame.event.get():
                if event.type==QUIT:
                    run=False

            if run==False:
                break

        draw(i,k,j)
        pygame.display.update()

        t=m
        numbers[k]=numbers[i]
        numbers[i]=t

        # print(numbers[i])

    if i==length:
        draw(INF,INF,INF)

    time_now=pygame.time.get_ticks()
    print(i+1,time_now-prev)
    prev=time_now

    i+=1


pygame.quit()