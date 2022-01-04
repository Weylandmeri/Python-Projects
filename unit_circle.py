import pygame
import math

pygame.init()
pygame.font.init()

WIDTH, HEIGHT = 700, 700
HALF = WIDTH/2
RADIUS = 200
PRECISION = 5
COLOR = "#FE53BB"
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.SysFont('calibri', 15)

class Circle:
	def __init__(self, radius, width):
		self.radius = radius
		self.width = width

	def draw(self):
		mouse_xy = 	pygame.mouse.get_pos()
		pygame.draw.circle(WINDOW, COLOR, (WIDTH/2, HEIGHT/2), self.radius, self.width)
		pygame.draw.line(WINDOW, COLOR, (HEIGHT/2-self.radius, WIDTH/2),(WIDTH/2+self.radius, HEIGHT/2), self.width)
		pygame.draw.line(WINDOW, COLOR, (HEIGHT/2, WIDTH/2-self.radius),(WIDTH/2, HEIGHT/2+self.radius), self.width)

circle = Circle(RADIUS, 1)

def draw_triangle():
	mouse_xy = pygame.mouse.get_pos()

	mouse_xy = (mouse_xy[0]-HALF, -(mouse_xy[1]-HALF))
	mouse_xy = (mouse_xy[0]+HALF, mouse_xy[1]+HALF)

	hypotenuse = math.sqrt((mouse_xy[0]-HALF)**2+(mouse_xy[1]-HALF)**2)

	try:
		cosine = (mouse_xy[0]-HEIGHT/2)/hypotenuse
	except ZeroDivisionError:
		cosine = float("nan")
	try:
		sine = (mouse_xy[1]-WIDTH/2)/hypotenuse
	except ZeroDivisionError:
		sine = float("nan")
	if cosine == 0:
		cosine = .00001
	tangent = sine/cosine
	if sine == 1 or sine == -1:
		cosine = 0
		tangent = float("inf")
	if sine == 0:
		tangent = 0
	#angle = math.atan(tangent)*(180/math.pi) # Alternative angle
	angle = math.atan2(mouse_xy[1]-HALF, mouse_xy[0]-HALF)*(180/math.pi)
	if angle < -angle:
		angle = (math.atan2(mouse_xy[1]-HALF, mouse_xy[0]-HALF)*(180/math.pi)+360)

	angeltext = font.render(f'Degrees: {round(angle, PRECISION)}°', True, "#F5D300")
	radtext = font.render(f'Radians: {round(math.radians(angle), PRECISION)}', True, "#F5D300")
	sinetext = font.render(f'Sine: {round(sine, PRECISION)}', True, "#F5D300")
	cosinetext = font.render(f'Cosine: {round(cosine, PRECISION)}', True, "#F5D300")
	tangenttext = font.render(f'Tangent: {round(tangent, PRECISION)}', True, "#F5D300")

	WINDOW.blit(angeltext,(WIDTH-120,5))
	WINDOW.blit(radtext,(WIDTH-120,30))
	WINDOW.blit(sinetext,(WIDTH-120,55))
	WINDOW.blit(cosinetext,(WIDTH-120,80))
	WINDOW.blit(tangenttext,(WIDTH-120,105))

	pygame.draw.line(WINDOW, "#F5D300", (HEIGHT/2, WIDTH/2), (RADIUS*cosine+HALF,-RADIUS*sine+HALF), 1)
	pygame.draw.line(WINDOW, "#F5D300", (RADIUS*cosine+HALF,-RADIUS*sine+HALF), (RADIUS*cosine+HALF,HALF), 1)
	pygame.draw.line(WINDOW, "#F5D300", (HEIGHT/2, WIDTH/2), (RADIUS*cosine+HALF,HALF), 1)

def main():
	running = True

	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
		WINDOW.fill("#212946")
		circle.draw()
		draw_triangle()
		pygame.display.update()

	pygame.quit()

if __name__ == "__main__":
	main()