import pygame
import numpy as np

pygame.init()

WIDTH, HEIGHT = 700, 700
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

def NormalizeData(data):
    return (data - np.min(data)) / (np.max(data) - np.min(data))

def bezier(point1, point2, point3, RESOLUTION):
	xvalues = NormalizeData(np.linspace(point1[0], point3[0], RESOLUTION))
	finalpoints = []
	for t in xvalues:
		xvalue = point1[0]*(t**2) + point2[0]*2*t*(1-t) + point3[0]*(1-t)**2
		yvalue = point1[1]*(t**2) + point2[1]*2*t*(1-t) + point3[1]*(1-t)**2
		finalpoints.append((xvalue, yvalue))
	for i in range(0, len(finalpoints)-1):
		pygame.draw.line(WINDOW, "#FE53BB", finalpoints[i],finalpoints[i+1], 5)
	pygame.draw.circle(WINDOW, "#F5D300", point1, 10)
	pygame.draw.circle(WINDOW, '#08F7FE', point2, 10)
	pygame.draw.circle(WINDOW, "#00ff41", point3, 10)

def main():
	running = True
	point1 = (100, 500)
	point2 = (350, 250)
	point3 = (600, 500)
	RESOLUTION = 500
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if pygame.mouse.get_pressed()[0] and WINDOW.get_at(pygame.mouse.get_pos()) == (245, 211, 0, 255):
				point1 = pygame.mouse.get_pos()
			if pygame.mouse.get_pressed()[0] and WINDOW.get_at(pygame.mouse.get_pos()) == (8, 247, 254, 255):
				point2 = pygame.mouse.get_pos()
			if pygame.mouse.get_pressed()[0] and WINDOW.get_at(pygame.mouse.get_pos()) == (0, 255, 65, 255):
				point3 = pygame.mouse.get_pos()

		WINDOW.fill("#212946")
		bezier(point1, point2, point3, RESOLUTION)
		pygame.display.update()
	pygame.quit()

if __name__ == "__main__":
	main()