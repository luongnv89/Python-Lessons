import pygame, sys
from pygame.locals import *
pygame.init()

FPS = 10 # frames per second
fpsClock = pygame.time.Clock()

WIDTH = 400
HEIGHT = 300

#setup the window
DISPLAYSURF = pygame.display.set_mode((400,300),0,32)
pygame.display.set_caption('Animation')

WHITE = (255,255,255)

boom = pygame.image.load('boom.png')
bx = 200
by = 5
explosion = pygame.image.load('explosion.png')
exploded = pygame.mixer.Sound('/Users/percevio/projects/python-test/dragon/sound.m4a')

direction = 'down'
# velocity = 'fast'

while True: # the main game loop
	DISPLAYSURF.fill(WHITE)
	img = boom
	if direction == 'down':
		by += 5
		if by >= HEIGHT - 32 :
			img = explosion
			exploded.play()
			direction = 'up'
	else:
		by -=5
		if by == 0 :
			direction = 'down'
	# if velocity == 'fast':
	# 	FPS += 1
	# 	if FPS == 90 :
	# 		velocity = 'slow'
	# else:
	# 	FPS -=1
	# 	if FPS == 30 :
	# 		velocity = 'fast'
	print("x= "+ str(bx) +"; y= "+str(by)+"; FPS = "+str(FPS))
	DISPLAYSURF.blit(img,(bx,by))
	for event in pygame.event.get():
		if event.type == QUIT:
				pygame.quit()
				sys.exit()

	pygame.display.update()
	fpsClock.tick(FPS)