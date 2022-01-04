import pygame
import numpy as np
import math

pygame.init()

image = pygame.image.load("shape.png")

WIDTH = image.get_width()
HEIGHT = image.get_height()

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

def get_pixels(pixel):
	x = pixel[0]
	y = pixel[1]
	L = (abs(x-1),y)
	T = (x,abs(y-1))
	R = (x+1,y)
	B = (x,y+1)
	return L,T,R,B

def get_value(pixel):
	return image.get_at(pixel)[0]

def NormalizeData(data):
	return (data - np.min(data)) / (np.max(data) - np.min(data))

vecx = []
vecy = []

for x in range(WIDTH-1):
	for y in range(HEIGHT-1):
			left, top, right, bottom = get_pixels((x,y))
			left, top, right, bottom = get_value(left),get_value(top),get_value(right),get_value(bottom)
			
			vecx.append((left-right))
			vecy.append((bottom-top))


vecx = NormalizeData(vecx)
vecy = NormalizeData(vecy)

finalcolors = []
for first, second in zip(vecx, vecy):
	red = first*255.999
	green = second*255.999
	blue = 255.999

	finalcolors.append((red, green, blue))

index = 0
for x in range(WIDTH-1):
	for y in range(HEIGHT-1):
		WINDOW.set_at((x,y), finalcolors[index])
		index +=1

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