import pygame
import random
import sys
from variable import *
from classes import *
from functions import *


window = pygame.display.set_mode((830, 620))
pygame.display.set_caption('Dungeon Of the Skeleton GOD')



start_screen = pygame.Surface((800, 600))
rect1 = pygame.Surface ((20,20))



pygame.font.init ()
font1= pygame.font.Font ("fonts/fonta.ttf", 24)


timer = pygame.time.Clock  ()
pygame.time.set_timer(event1+1, 3000)


def main_loop ():


	c = 5
	x = 0
	done = True
	xx = 0
	xxx = 0

	while done:

		for e in pygame.event.get ():
				if e.type == pygame.QUIT:
					sys.exit ()
				if e.type == event1+1:
					c = x

		

		



		window.blit(start_screen, (10, 10))
		start_screen.fill ((123,12,45))


		xx += 1
		x += timer.tick (30)
		start_screen.blit (rect1, ((x/30),100))		
		rect1.fill ((xx,xx,xx))


		#moving_rect (x, xx)
		
		b = pygame.time.get_ticks ()		
		a = timer.get_fps()
		start_screen.blit(font1.render (str(a), True, (250,250,250)),(0,0))

		start_screen.blit(font1.render (str(b), True, (250,250,250)),(15,15))
		start_screen.blit(font1.render (str(x), True, (250,250,250)),(30,30))
		start_screen.blit(font1.render (str(c), True, (250,250,250)),(100,30))
		#pygame.time.delay(60)

		pygame.display.flip() 



main_loop ()









