#imports
import pygame, math, json
from pygame.locals import *
from config import *

#setup code
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#world object
class World(object):
	def __init__(self, screen, bgcolor):
		self.screen = screen
		self.bgcolor = bgcolor
		
	def render(self):
		self.screen.fill(self.bgcolor)
		
#menu object
class Menu(object):
	def __init__(self, screen, bgcolor):
		self.screen = screen
		self.bgcolor = bgcolor
		
	def render(self):
		self.screen.fill(self.bgcolor)

world = World(screen, (255,255,200))


#main game loop
running = True
font = pygame.font.Font("PressStart2P.ttf", FONTSIZE) 
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
	print clock.get_time()
	clock.tick()
	
	world.render()
	
	#if FPS is on, render it
	if SHOWFPS:
		fps = clock.get_fps()
		try:
			if math.isinf(fps):
				fps = 10000.0
			screen.blit(font.render("%0.1f" % fps, False, (255,255,255),  (0,0,0)), (200,200))
		except: pass
	pygame.display.update()