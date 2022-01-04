import pygame
import numpy as np
import math

pygame.init()

sigma = 100
WIDTH = 256 # half the window
WINDOW = pygame.display.set_mode((WIDTH*2, WIDTH*2))

X = range(-WIDTH, WIDTH)
Y = range(-WIDTH, WIDTH)

def NormalizeData(data):
    return (data - np.min(data)) / (np.max(data) - np.min(data))

color = []

for x in X:
	for y in Y:
		try: # where the magic happens!   
			#z = (1/(2*math.pi*sigma**2))*math.e**(-(x**2+y**2)/(2*sigma**2)) # normal distribution
			#z = math.sqrt(-x**2-y**2+200**2) # Sphere
			z = math.sqrt(200*math.sqrt(x**2+y**2)-x**2-y**2-7500) # Torus
			#z = -abs(x*math.cos(math.pi/4)-y*math.sin(math.pi/4)) + -abs(x*math.sin(math.pi/4)+y*math.cos(math.pi/4)) # pyramid
			#z = (1-x/200)**2 + 100*(y/200-(x/200)**2)**2 #Rosenbrock function
			#z = (1.5-x+x*y)**2  + (2.25 - x + x*y**2)**2 + (2.625 -x + x*y**3)**2 #Beale function
			#z = (x**2 + y + 11)**2 + (x+y**2 - 7)**2
			#z = x**2 + y**2 #parabaloid
			#z = math.sin(x/25)+math.sin(y/25) # sine wave pattern
			#z = .5 + (math.sin(x**2-y**2)**2- .5)/(abs(1+.001*(x**2+y**2)))**2
			#z = math.sqrt(x**2 + y**2 - 20000) # looking into a well
			#z = -math.sqrt(x**2 + y**2 - 20000) - math.sqrt(-x**2-y**2+200**2) # interesting pattern
			#z = math.sqrt(x**2 + y**2) # cone
			#z = x*y/(x**2 + y**2) # anisotrpic pattern
			#z  = x/y/x/y
		except (ZeroDivisionError, ValueError, OverflowError):
			z = 1
		color.append(z)

color = NormalizeData(color)
#color = [x*255 for x in color]
#colors = [[x, x, x] for x in color]


def lerp_color(colors, value):
	fract, index = math.modf(value)
	color1 = pygame.Color(colors[int(index) % len(colors)])
	color2 = pygame.Color(colors[int(index + 1) % len(colors)])
	return color1.lerp(color2, fract)

colors = []
#colors = ["blue", "green", "yellow", "red"]
colors = [(161,38,34), (255,248,196)]
for i in color:
	current_color = lerp_color(colors, i)
	colors.append(current_color)

index = 0
for x in X:
	for y in Y:
		WINDOW.set_at((x+WIDTH, y+WIDTH), colors[index])
		index+=1

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
