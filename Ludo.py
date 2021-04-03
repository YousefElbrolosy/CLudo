import pygame
import random
import time

pygame.init()
pygame.display.set_caption("Ludo")
screen = pygame.display.set_mode((680, 600))

board = pygame.image.load('Board.jpg')
one = pygame.image.load('1.png')
two = pygame.image.load('2.png')
three = pygame.image.load('3.png')
four = pygame.image.load('4.png')
five = pygame.image.load('5.png')
six = pygame.image.load('6.png')

dice=[one,two,three,four,five,six]



red = pygame.image.load('red.png')
blue = pygame.image.load('blue.png')
green = pygame.image.load('green.png')
yellow = pygame.image.load('yellow.png')

color=[red,green,yellow,blue]

HOME = [[(110, 58), (61, 107), (152, 107), (110, 152)],   # Red
        [(466, 58), (418, 107), (509, 107), (466, 153)],  # Green
        [(466, 415), (418, 464), (509, 464), (466, 510)], # Yellow
        [(110, 415), (61, 464), (152, 464), (110, 510)]]  # Blue

SAFE=[(50,240),(328, 50),(520, 329),(241, 520)] 

position=HOME

def display(colour, position):
    screen.blit(colour, position)

def roll_Dice():
    return random.randint(1,6)

def move_token(x,y):
    for i in range(len(HOME)):
        if position[x][y] in HOME[i]:
            if number==6:
                position[x][y]=SAFE[i]

               
            
    
    

number=1
running = True
while(running):
    screen.fill((255,255,255))
    screen.blit(board, (0, 0))

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type==pygame.MOUSEBUTTONUP:
            
            coordinate=pygame.mouse.get_pos()
#             for i in range(6):
#                 number=roll_Dice()
#                 time.sleep(0.1)
#                 screen.blit(number, (605, 270))
# #                 time.sleep(0.001)
#                 pygame.display.update()
            if (605<=coordinate[0]<=669) and (270<=coordinate[1]<=334):
                number=roll_Dice()
                
    screen.blit(dice[number-1], (605, 270))
            
    for i in range(len(position)):
        for j in position[i]:
            screen.blit(color[i], j)
        

    pygame.display.update()