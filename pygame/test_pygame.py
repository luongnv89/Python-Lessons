import pygame, sys, time
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((500, 400),0,32)
pygame.display.set_caption('Hello')
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)
mycolors =[BLACK, BLUE, GREEN, WHITE, RED]
DISPLAYSURF.fill(BLACK)
pygame.draw.polygon(DISPLAYSURF, GREEN, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)),2)
myrect = pygame.Rect(0,0,10,10);
pygame.draw.circle(DISPLAYSURF, BLUE, (300, 50), 20, 3)
pygame.draw.ellipse(DISPLAYSURF, RED, (100, 250, 200, 80), 4)
# i = 0
while True: # main game loop
	# i +=1
	pygame.draw.rect(DISPLAYSURF, RED, myrect,1)
	myrect.left +=5
	# DISPLAYSURF.fill(i%4)
	for event in pygame.event.get():
	    if event.type == QUIT:
	        pygame.quit()
	        sys.exit()
	pygame.display.update()
	time.sleep(1)