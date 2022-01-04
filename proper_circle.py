import pygame
import numpy as np
import math

pygame.init()

RADIUS = 200
COLOR = "#F5D300"

WINDOW = pygame.display.set_mode((RADIUS*2, RADIUS*2))
WINDOW.fill("#212946")

X = range(-RADIUS, RADIUS)
Y = range(-RADIUS, RADIUS)

for x in X:
	for y in Y: # where the magic happens
		if math.sqrt((x)**2 + (y)**2) < RADIUS:
			WINDOW.set_at((x+RADIUS,y+RADIUS), COLOR)

def main():
	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
		pygame.display.update()
	pygame.quit()

if __name__ == "__main__":
	main()