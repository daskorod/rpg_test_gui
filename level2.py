import pygame
import pyganim
from functions import create_level
from screens import *
from constants import *


pygame.font.init ()
font1= pygame.font.Font ("fonts/fonta.ttf", 24)
rect1 = pygame.Surface ((20,20))

timer = pygame.time.Clock  ()
pygame.font.init ()
font1= pygame.font.Font ("fonts/fonta.ttf", 24)
rect1 = pygame.Surface ((20,20))
	
timer = pygame.time.Clock  ()


lev = [
       "",
       "",
       "",
       "",
       "",
       "              ",
       "  ---           ----  ",
       "   -----          ---- ",
       "      ----       ----  ",
       "--------------------------"]


class Level2 ():

	def __init__ (self, control):

	    self.platforms, self.block_group = create_level (lev)
	    self.control = control


	def render_stage (self):

		window.blit(start_screen, (10, 10))
		start_screen.fill ((black))
		start_screen.blit (adventure_screen, (0,0))
		start_screen.blit (instrumental_screen, (0,450))
		instrumental_screen.blit (hero_screen, (0,0))
		hero_screen.fill ((cool_orange))
		instrumental_screen.blit (information_screen, (150,0))
		information_screen.fill ((50,50,50))
		instrumental_screen.blit (monster_screen, (650,0))
		monster_screen.fill ((sea_color))
		adventure_screen.blit(background, (0, 0))

		self.block_group.draw (adventure_screen)
		start_screen.blit(font1.render (str(self.a), True, (250,250,250)),(0,0))
		


	def stage_loop (self):


		self.a = timer.get_fps()
		self.render_stage ()
		

		if self.control.k_space == True:
			self.control.stage2_flag = False
			self.control.stage1_flag = True

	
		timer.tick (30)
	