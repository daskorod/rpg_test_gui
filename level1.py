import pygame
import pyganim
import classes
from functions import create_level
from screens import *
from constants import *
import fonts


timer = pygame.time.Clock  ()
pygame.key.set_repeat(100,100)
pygame.key.get_repeat ()

lev = [
	       "",
	       "ccccccc",
	       "cccccccсссcссс",
	       "  сcccccc ccc c ",
	       "cccc m",
	       "    c  c cc  --- с    ",
	       " ---0-  -----  m        ----  ",
	       "   -----  c   ----     ---- ",
	       " m   cc 	с ccc    ----  ",
	       "--------------------------"]


class Level1 ():

	def __init__ (self, control, hero):
		self.platforms, self.block_group = create_level (lev)
		self.control = control
		self.hero = hero
		#self.hero.block_group = self.block_group

	def render_stage1 (self):

		window.blit(start_screen, (10, 10))
		start_screen.fill ((black))
		start_screen.blit (adventure_screen, (0,0))
		adventure_screen.fill ((black))
		start_screen.blit (instrumental_screen, (0,450))
		instrumental_screen.blit (hero_screen, (0,0))
		hero_screen.fill ((cool_orange))

		instrumental_screen.blit (information_screen, (150,0))
		#information_screen.fill ((50,50,50))
		instrumental_screen.blit (monster_screen, (650,0))
		monster_screen.fill ((sea_color))

		self.block_group.draw (adventure_screen)
		start_screen.blit(fonts.font1.render (str(self.a), True, (250,250,250)),(0,0))
		


	def stage_loop (self):


		self.a = timer.get_fps()
		
		self.render_stage1 ()

		self.hero.render (adventure_screen)
		self.hero.update (self.block_group)
		#self.hero.taking (self.block_group)


		timer.tick (60)

		if self.control.k_space == True:
			self.control.stage1_flag = False
			self.control.stage2_flag = True
