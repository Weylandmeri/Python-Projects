import pygame
import numpy as np
import math

pygame.init()

WIDTH, HEIGHT = 700, 700
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
color = '#F5D300'
background_color = '#212946'
linewidth = 2

# Cube vertices
cube = np.array([[100,100,100],[-100,100,100],[100,-100,100],[-100,-100,100],[-100,-100,-100],[-100,100,-100],[100,-100,-100],[100,100,-100]])

class shape:
	def __init__(self, vertices):
		self.vertices = vertices

	def rotatex(self, degrees):
		rotationx = np.array([[1,0,0], [0, math.cos(degrees), -math.sin(degrees)], [0, math.sin(degrees), math.cos(degrees)]])
		empty = []
		for i in self.vertices:
			x = np.matmul(rotationx, i)
			empty.append(x)
		self.vertices = np.array(empty)

	def rotatey(self, degrees):
		rotationy = np.array([[math.cos(degrees),0,math.sin(degrees)], [0, 1, 0], [-math.sin(degrees), 0, math.cos(degrees)]])
		empty = []
		for i in self.vertices:
			x = np.matmul(rotationy, i)
			empty.append(x)
		self.vertices = np.array(empty)

	def rotatez(self, degrees):
		rotationz = np.array([[math.cos(degrees),-math.sin(degrees),0], [math.sin(degrees), math.cos(degrees), 0], [0, 0, 1]])
		empty = []
		for i in self.vertices:
			x = np.matmul(rotationz, i)
			empty.append(x)
		self.vertices = np.array(empty)

	def orthographic(self):
		projection = np.array([[1,0,0],[0,1,0],[0,0,0]])
		empty = []
		for i in self.vertices:
			x = np.matmul(projection, i)
			empty.append(x)
		empty = np.array(empty)
		return empty

	def perspective(self):
		transformed = []
		c = np.array([0,0,350]) # Kind of like the focal length.
		e = np.array([0,0,350]) # Kind of like how close you get to the cube.
		for i in self.vertices: 
			x = np.subtract(i, c)
			transformed.append(x)
		x = []
		y = []
		for d in transformed:
			x.append(((e[2]/d[2])*d[0]+e[0]))
			y.append(((e[2]/d[2])*d[1]+e[1]))
		return x, y

Cube = shape(cube)

# Inititial Rotation to make it more interesting
#Cube.rotatex(math.pi/4)

def main():
	running = True
	while running:
		for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False
		x, y = Cube.perspective()

		Vertices = list(zip(x,y))
		WINDOW.fill(background_color)

		speed = .0003
		Cube.rotatex(-speed)
		Cube.rotatey(-speed)
		Cube.rotatez(-speed)

		# Draw Pygame Line connecting the transformed vertices + 350 to center them
		pygame.draw.line(WINDOW, color, (Vertices[0][0]+350, Vertices[0][1]+350), (Vertices[1][0]+350, Vertices[1][1]+350), linewidth)
		pygame.draw.line(WINDOW, color, (Vertices[1][0]+350, Vertices[1][1]+350), (Vertices[3][0]+350, Vertices[3][1]+350), linewidth)
		pygame.draw.line(WINDOW, color, (Vertices[3][0]+350, Vertices[3][1]+350), (Vertices[2][0]+350, Vertices[2][1]+350), linewidth)
		pygame.draw.line(WINDOW, color, (Vertices[0][0]+350, Vertices[0][1]+350), (Vertices[2][0]+350, Vertices[2][1]+350), linewidth)
		pygame.draw.line(WINDOW, color, (Vertices[0][0]+350, Vertices[0][1]+350), (Vertices[7][0]+350, Vertices[7][1]+350), linewidth)
		pygame.draw.line(WINDOW, color, (Vertices[1][0]+350, Vertices[1][1]+350), (Vertices[5][0]+350, Vertices[5][1]+350), linewidth)
		pygame.draw.line(WINDOW, color, (Vertices[3][0]+350, Vertices[3][1]+350), (Vertices[4][0]+350, Vertices[4][1]+350), linewidth)
		pygame.draw.line(WINDOW, color, (Vertices[2][0]+350, Vertices[2][1]+350), (Vertices[6][0]+350, Vertices[6][1]+350), linewidth)
		pygame.draw.line(WINDOW, color, (Vertices[7][0]+350, Vertices[7][1]+350), (Vertices[5][0]+350, Vertices[5][1]+350), linewidth)
		pygame.draw.line(WINDOW, color, (Vertices[5][0]+350, Vertices[5][1]+350), (Vertices[4][0]+350, Vertices[4][1]+350), linewidth)
		pygame.draw.line(WINDOW, color, (Vertices[4][0]+350, Vertices[4][1]+350), (Vertices[6][0]+350, Vertices[6][1]+350), linewidth)
		pygame.draw.line(WINDOW, color, (Vertices[6][0]+350, Vertices[6][1]+350), (Vertices[7][0]+350, Vertices[7][1]+350), linewidth)
		pygame.display.update()

	pygame.quit()

if __name__ == "__main__":
	main()