import pygame,sys,random
from pygame.locals import * 	
pygame.init()

Display = pygame.display.set_mode((400,400))
while True:
	for event in pygame.event.get():
		if event.type == QUIT :
			pygame.quit()
			sys.exit()
