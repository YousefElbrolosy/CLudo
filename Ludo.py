import pygame

pygame.init()
pygame.display.set_caption("Ludo")
screen = pygame.display.set_mode((600, 600))

board = pygame.image.load('Board.jpg')

red = pygame.image.load('red.png')
blue = pygame.image.load('blue.png')
green = pygame.image.load('green.png')
yellow = pygame.image.load('yellow1.png')

HOME = [[(110, 58), (61, 107), (152, 107), (110, 152)],   # Red
        [(466, 58), (418, 107), (509, 107), (466, 153)],  # Green
        [(110, 415), (61, 464), (152, 464), (110, 510)],  # Blue
        [(466, 415), (418, 464), (509, 464), (466, 510)]] # Yellow

def display(colour, position):
    screen.blit(colour, position)

running = True
while(running):
    screen.blit(board, (0, 0))
    screen.blit(yellow, (466, 510))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        

    pygame.display.update()