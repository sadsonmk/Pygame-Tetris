import pygame,sys
from pygame.locals import *
from copy import deepcopy


pygame.init()
ROWS,COLS = 20,10
SQUARE = 35
RES = COLS*SQUARE,ROWS*SQUARE

# framerate per second (fps)
FPS = 60
clock_fps = pygame.time.Clock()

# colors
color1 = 'red'
color2 = (0,255,0) 
color3 = Color('#0000ff')
black = (0,0,0)

game_screen = pygame.display.set_mode(RES)
pygame.display.set_caption('Tetris Game')

def draw_grid():
    for x in range(0,COLS):
        for y in range(0,ROWS):
            grid = pygame.Rect(x*SQUARE,y*SQUARE,SQUARE,SQUARE)
            pygame.draw.rect(game_screen,[40,40,40],grid,1)

pieces = [[(0,0),(0,-1),(-1,-1),(-1,0)],
          [(0,0),(0,1),(-1,-1),(-1,0)],
          [(0,0),(0,1),(0,-1),(-1,0)],
          [(-1,0),(-2,0),(0,0),(1,0)],
          [(0,0),(-1,1),(0,-1),(-1,0)],
          [(0,0),(0,1),(0,-1),(-1,1)],
          [(-1,0),(-1,1),(0,1),(-1,-1)]]

pieces_rect = [[pygame.Rect(x+COLS//2,y+1,1,1) for x,y in piece] for piece in pieces]

shape = deepcopy(pieces_rect[1])
shape_rect = pygame.Rect(0,0,SQUARE-2,SQUARE-2)
count,speed,limit = 0,50,1500

# game loop
while True:

    dx = 0
    game_screen.fill(black)
    #handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -1
            if event.key == pygame.K_RIGHT:
                dx = 1
            if event.key == pygame.K_DOWN:
                limit = 100
    
    draw_grid()

    # x movement
    old_shape = deepcopy(shape)
    for i in range(4):
        shape[i].x += dx
        if shape[i].x < 0 or shape[i].x > COLS-1:
           shape = deepcopy(old_shape)
           break
        
    # y movement
    count += speed
    if count > limit:
        count = 0
        old_shape = deepcopy(shape)
        for i in range(4):
            shape[i].y += 1
            if shape[i].x < 0 or shape[i].x > COLS-1:
                shape = deepcopy(old_shape)
                limit = 1500
                break
            
                


    
       
    for i in range(4):
        shape_rect.x = shape[i].x*SQUARE
        shape_rect.y = shape[i].y*SQUARE
        pygame.draw.rect(game_screen,[255,255,255],shape_rect)
    
    # update the surface
    pygame.display.flip()
   
    clock_fps.tick(FPS)
    
pygame.quit()

