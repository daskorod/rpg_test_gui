import pygame
import pyganim
import classes
from functions import create_level
from screens import *
from constants import *

pygame.font.init ()
font1= pygame.font.Font ("fonts/fonta.ttf", 24)
rect1 = pygame.Surface ((20,20))
timer = pygame.time.Clock  ()

svin_anim_list = [('images/svin_motion.png',0.5),('images/svin_motion2.png',0.3),('images/svin_motion3.png',0.2)]
svin_anim = pyganim.PygAnimation(svin_anim_list)
svin_anim.play ()

lev = [
       "------------------------",
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

	def __init__ (self, control,hero):

	    self.platforms, self.block_group, self.chests = create_level (lev)
	    self.control = control
	    self.hero = hero
	    #self.hero.block_group = self.block_group

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

		svin_anim.blit (adventure_screen, (10,10))

		self.hero.render (adventure_screen)
		self.hero.update (self.platforms)	



		if self.control.k_space == True:
			self.control.stage2_flag = False
			self.control.stage1_flag = True

		timer.tick (30)
	