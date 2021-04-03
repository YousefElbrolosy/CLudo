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

dice = [one, two, three, four, five, six]


red = pygame.image.load('red.png')
blue = pygame.image.load('blue.png')
green = pygame.image.load('green.png')
yellow = pygame.image.load('yellow.png')

color = [red, green, yellow, blue]
number = 1

HOME = [[(110, 58), (61, 107), (152, 107), (110, 152)],   # Red
        [(466, 58), (418, 107), (509, 107), (466, 153)],  # Green
        [(466, 415), (418, 464), (509, 464), (466, 510)],  # Yellow
        [(110, 415), (61, 464), (152, 464), (110, 510)]]  # Blue

SAFE = [(50, 240), (328, 50), (520, 328), (241, 520)]

position = [[[110, 58], [61, 107], [152, 107], [110, 152],[50,328],[50,284]],   # Red
           [[466, 58], [418, 107], [509, 107], [466, 153]],  # Green
           [[466, 415], [418, 464], [509, 464], [466, 510],[50,328],[520,240]],  # Yellow
           [[110, 415], [61, 464], [152, 464], [110, 510]]]  # Blue
# position=HOME

def move_token(x, y):
    flag=True
    for i in range(len(HOME)):
        if tuple(position[x][y]) in HOME[i]:
            if number == 6:
                position[x][y] = list(SAFE[i])
                flag=False
                break

    if flag:
        for _ in range(number):
            #  R1,Y1
            if (position[x][y][1] == 240 and position[x][y][0] < 202) or (position[x][y][1] == 240 and 368<=position[x][y][0] < 558):
                position[x][y][0] += 38
            #  R2
            elif (position[x][y][1] == 284 and position[x][y][0] < 202 and x==0) :
                position[x][y][0] += 38
            # R3->R2->R1
            elif (position[x][y][0] == 12 and position[x][y][1] > 240):
                position[x][y][1] -= 44

            #  R3,Y3
            elif (position[x][y][1] == 328 and 12<position[x][y][0] <= 202) or (position[x][y][1] == 328 and 368<position[x][y][0]):
                position[x][y][0] -= 38
            #  Y2
            elif  position[x][y][1] == 284 and 368<position[x][y][0] and x==2:
                position[x][y][0] -= 38
            #  Y1->Y2->Y3
            elif (position[x][y][0] == 558 and position[x][y][1] <328):
                position[x][y][1] += 44


running = True
while(running):
    screen.fill((255, 255, 255))
    screen.blit(board, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            coordinate = pygame.mouse.get_pos()
            if (605 <= coordinate[0] <= 669) and (270 <= coordinate[1] <= 334):
                number = random.randint(1, 6)
            else:
                for i in range(len(position)):
                    for j in range(len(position[i])):
                        if position[i][j][0] <= coordinate[0] <= position[i][j][0]+31 and position[i][j][1] <= coordinate[1] <= position[i][j][1]+31:
                            move_token(i, j)

    screen.blit(dice[number-1], (605, 270))

    for i in range(len(position)):
        for j in position[i]:
            screen.blit(color[i], j)
    

    pygame.display.update()
