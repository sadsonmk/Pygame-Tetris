import pygame
from pygame.locals import *
from copy import deepcopy
import random

ROWS,COLS = 20,10
TILE = 35
GAME_RES = COLS *TILE,ROWS * TILE
FPS = 60

pygame.init()
game_sc = pygame.display.set_mode(GAME_RES)
clock = pygame.time.Clock()

grid = [pygame.Rect(x*TILE,y*TILE,TILE,TILE) for x in range(COLS) for y in range(ROWS)]


figure_pos = [[(0,0),(0,-1),(-1,-1),(-1,0)],
          [(0,0),(0,1),(-1,-1),(-1,0)],
          [(0,0),(0,1),(0,-1),(-1,0)],
          [(-1,0),(-2,0),(0,0),(1,0)],
          [(0,0),(-1,1),(0,-1),(-1,0)],
          [(0,0),(0,1),(0,-1),(-1,1)],
          [(-1,0),(-1,1),(0,1),(-1,-1)]]

figures = [[pygame.Rect(x+COLS//2,y+1,1,1) for x,y in fig_pos] for fig_pos in figure_pos]

figure_rect = pygame.Rect(0,0,TILE-2,TILE-2)

play_field = [[0 for i in range(COLS)] for j in range(ROWS)]

anim_count,anim_speed,anim_limit = 0,60,2000
figure = deepcopy(random.choice(figures))

def check_edges():
    if figure[i].x < 0 or figure[i].x > COLS-1:
        return False
    elif figure[i].y > ROWS -1 or play_field[figure[i].y][figure[i].x]:
        return False
    return True

while True:
    dx = 0
    rotate = False
    game_sc.fill(pygame.Color('#000000'))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -1
            elif event.key == pygame.K_RIGHT:
                dx = 1
            elif event.key == pygame.K_DOWN:
                anim_limit = 100
            elif event.key == pygame.K_UP:
                rotate = True

    # move x
    figure_old = deepcopy(figure)
    for i in range(4):
        figure[i].x += dx
        if not check_edges():
            figure = deepcopy(figure_old)
            break
    
    # move y
    anim_count += anim_speed
    if anim_count > anim_limit:
        anim_count = 0
        figure_old = deepcopy(figure)
        for i in range(4):
            figure[i].y += 1
            if not check_edges():
                for i in range(4):
                    play_field[figure_old[i].y][figure_old[i].x] = pygame.Color('white')
                figure = deepcopy(random.choice(figures))
                anim_limit = 2000
                break

    # rotate
    center = figure[0]
    figure_old = deepcopy(figure)
    if rotate:
        for i in range(4):
            x = figure[i].y - center.y
            y = figure[i].x - center.x
            figure[i].x = center.x - x
            figure[i].y = center.y + y
            if not check_edges():
                figure = deepcopy(figure_old)
                break
    [pygame.draw.rect(game_sc,(30,30,30),rect_1,1 ) for rect_1 in grid] 

    for i in range(4):
        figure_rect.x = figure[i].x*TILE
        figure_rect.y = figure[i].y*TILE
        pygame.draw.rect(game_sc,pygame.Color('#ffffff'),figure_rect)
    for y, raw in enumerate(play_field):
        for x ,col in enumerate(raw):
            if col:
                figure_rect.x,figure_rect.y = x*TILE,y*TILE
                pygame.draw.rect(game_sc,col,figure_rect)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()