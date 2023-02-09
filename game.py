import pygame
from pygame.locals import *

res = width,height = 800,750
road_width = width//2
marking_width = width//80
pygame.init()


pygame.display.set_caption("Racing game")
win = pygame.display.set_mode(res)

win.fill(Color(0,0,0))

running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    pygame.draw.rect(win,[50,50,50],(width/2-road_width/2,0,road_width,height))
    pygame.draw.rect(win,[255,250,60],(width/2-marking_width/2,0,marking_width,height))
    pygame.draw.rect(win,[255,255,255],(width/2-road_width/2 + marking_width*3,0,marking_width,height))
    pygame.draw.rect(win,[255,255,255],(width/2+road_width/2 - marking_width*4,0,marking_width,height))

    pygame.display.update()
pygame.quit()