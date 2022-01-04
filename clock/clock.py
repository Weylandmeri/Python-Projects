import sys
import pygame
import math
from pygame import *
from datetime import datetime

pygame.init()

def scale_image(img, factor):
	size = round(img.get_width()*factor), round(img.get_height()*factor)
	return pygame.transform.smoothscale(img, size)

def rotate_image(img, degrees, scale):
	return pygame.transform.rotozoom(img, -(degrees), scale)


CLOCK_IMAGE = scale_image(pygame.image.load("images/clock_background_3.png"), .5)
HOUR_HAND = scale_image(pygame.image.load("images/hour.png"), .5)
MINUTE_HAND = scale_image(pygame.image.load("images/minute.png"), .5)
SECOND_HAND = scale_image(pygame.image.load("images/second.png"), .5)

WIDTH, HEIGHT = 512, 512
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Clock")
fps = 60

def main():
	while True:
		now = datetime.now().strftime("%H:%M:%S")
		second = int(now[6:8])
		minute = int(now[3:5]) + second/60
		hour = int(now[:2]) + minute/60

		if hour > 12:
			hour -= 12
		hour = hour*5
		
		hour_angle = hour*6
		minute_angle = minute*6
		second_angle = second*6

		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

		fpsClock = pygame.time.Clock()

		color = pygame.Color("#212946")
		number = pygame.time.get_ticks()

		screen.fill(color)

		rotating_hour = rotate_image(HOUR_HAND, hour_angle, 1)
		rotating_minute = rotate_image(MINUTE_HAND, minute_angle, 1)
		rotating_second = rotate_image(SECOND_HAND, second_angle, 1)

		screen.blit(CLOCK_IMAGE, (0,0))
		screen.blit(rotating_hour, (WIDTH/2 - int(rotating_hour.get_width()/2), HEIGHT/2 - int(rotating_hour.get_height()/2)))
		screen.blit(rotating_minute, (WIDTH/2 - int(rotating_minute.get_width()/2), HEIGHT/2 - int(rotating_minute.get_height()/2)))
		screen.blit(rotating_second, (WIDTH/2 - int(rotating_second.get_width()/2), HEIGHT/2 - int(rotating_second.get_height()/2)))
		pygame.display.update()

		pygame.display.flip()
		fpsClock.tick(fps)

if __name__ == "__main__":
	main()