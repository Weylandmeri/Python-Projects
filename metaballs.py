import pygame
import numpy as np
import math

pygame.init()

WIDTH = 75

WINDOW = pygame.display.set_mode((WIDTH*2, WIDTH*2))

WINDOW.fill("#212946")

X = np.arange(-WIDTH, WIDTH)
Y = X

clock = pygame.time.Clock()

def metaball(loc1):
	for x in X:
		for y in Y:
			if 1/((x - loc1[0])**2+(y - loc1[1])**2) + 1/((x-25)**2+(y-25)**2) > .001:
				WINDOW.set_at((x+WIDTH,y+WIDTH), "#F5D300")

def main():
	running = True
	holding = False
	loc1 = (-25, -25)
	while running:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.MOUSEBUTTONDOWN:
				holding = True
			if event.type == pygame.MOUSEBUTTONUP:
				holding = False
			if holding:
				mouse = pygame.mouse.get_pos()
				loc1 = (mouse[0]-WIDTH, mouse[1]-WIDTH)

		WINDOW.fill("#212946")
		metaball(loc1)
		pygame.display.update()
	pygame.quit()

if __name__ == "__main__":
	main()