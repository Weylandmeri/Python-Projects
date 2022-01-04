import pygame
import numpy as np

pygame.init()

WIDTH, HEIGHT = 700, 700

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

def set_pallete():
	pallete = pygame.image.load("pallete.png")
	pallete = pygame.transform.scale(pallete, (200, 100))
	pygame.Surface.blit(WINDOW, pallete, (0,0))

set_pallete()

def main():
	running = True

	color = (25, 0, 160)
	try:
		last_image = pygame.image.load("renders/image.png")
	except FileNotFoundError:
		pass

	while running:
		mouse_xy = pygame.mouse.get_pos()
		mouse = pygame.mouse.get_rel()
		mouse = (mouse_xy[0]+mouse[0], mouse_xy[1]+mouse[1])

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.MOUSEBUTTONUP:
				pygame.image.save(WINDOW, "renders/image.png")		

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				WINDOW.fill((0,0,0))
				set_pallete()

			if event.key == pygame.K_z and pygame.key.get_mods() & pygame.K_LCTRL:
				pygame.Surface.blit(WINDOW, last_image, (0,0))
				

		if pygame.mouse.get_pressed()[2] and WINDOW.get_at(mouse_xy) != (0,0,0):
			color = WINDOW.get_at(mouse_xy)

		if pygame.mouse.get_pressed()[0]:
			WINDOW.set_at(mouse_xy, color)
			WINDOW.set_at(((mouse_xy[0]+1, mouse_xy[1]+1)), color)
			WINDOW.set_at(((mouse_xy[0]-1, mouse_xy[1]-1)), color)
			WINDOW.set_at(((mouse_xy[0]-1, mouse_xy[1]+1)), color)
			WINDOW.set_at(((mouse_xy[0]+1, mouse_xy[1]-1)), color)
			WINDOW.set_at(((mouse_xy[0]+1, mouse_xy[1])), color)
			WINDOW.set_at(((mouse_xy[0], mouse_xy[1]+1)), color)
			WINDOW.set_at(((mouse_xy[0]-1, mouse_xy[1])), color)
			WINDOW.set_at(((mouse_xy[0], mouse_xy[1]-1)), color)


			pygame.draw.line(WINDOW, color, mouse_xy, mouse)

		pygame.display.update()


	WINDOW.fill((0,0,0))
	set_pallete()
	pygame.display.update()

	pygame.image.save(WINDOW, "renders/image.png")

	pygame.quit()

if __name__ == "__main__":
	main()