#imports
import pygame
from pygame.locals import *
from config import *
#setup code
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))




#main game loop
running = True
font = pygame.font.Font("PressStart2P.ttf", 10) 
clock = pygame.time.Clock()

while running:
	keys = []
	#event processing
	for event in pygame.event.get():
		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				pygame.quit()
				running = False
			else:
				keys.append(event.key)
		if event.type == QUIT:
			pygame.quit()
			running = False
	if not running: break

	#determine the # of game ticks since last frame.
	
	clock.tick()
	
	
	screen.fill((0,255,255))
	
	#if FPS is on, render it
	if SHOWFPS:
		fps = clock.get_fps()
		try:
			screen.blit(font.render("%0.1f" % fps, False, (255,255,255)), (200,200))
		except: pass
	pygame.display.update()