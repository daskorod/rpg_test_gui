
import pygame
import random
import sys
import pyganim
from constants import *
from classes import Platform
from classes import Monster
from functions import event_go
from screens import *



#Font

pygame.font.init ()
font1= pygame.font.Font ("fonts/fonta.ttf", 24)
rect1 = pygame.Surface ((20,20))

#Timer

timer = pygame.time.Clock  ()

#Animation

svin_anim_list = [('images/svin_motion.png',0.5),('images/svin_motion2.png',0.3),('images/svin_motion3.png',0.2)]
svin_anim = pyganim.PygAnimation(svin_anim_list)
svin_anim.play ()


lev1 = [
       "",
       "",
       "",
       "",
       "",
       "              ",
       "             ----  ",
       "             ---- ",
       "             ----  ",
       "--------------------------"]

lev2 = [
       "",
       "",
       "",
       "",
       "",
       "              ",
       "              ",
       "    ----          ",
       "  ---   ---         ",
       "--------------------------"]
#Group for represent
#units = pygame.sprite.Group ()
#units.add ()

class Main ():
	def __init__ (self):
		pass
		self.x = 0
		self.y = 0
		self.platforms = []
		self.platforms2 = []
		self.block_group = pygame.sprite.Group ()
		self.block_group2 = pygame.sprite.Group ()
		self.done = True
		self.constructor = False
		self.constructor2 = False
		self.constructor3 = False
		self.stage1 = True
		self.stage2 = False
		self.stage3 = False
		self.k_space = False

	def create_level (self, level):
		for row in level:
			for col in row:
				if col == "-":
					pf = Platform (self.x,self.y)
					self.platforms.append (pf)
					self.block_group.add (pf)
				self.x += 45
			self.x = 0
			self.y += 45
		self.x = 0
		self.y = 0

	def create_level2 (self, level):
		for row in level:
			for col in row:
				if col == "-":
					pf = Platform (self.x,self.y)
					self.platforms.append (pf)
					self.block_group2.add (pf)
				self.x += 45
			self.x = 0
			self.y += 45
		self.x = 0
		self.y = 0

	def render_main (self):
			
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

	def render_stage1 (self):

		adventure_screen.blit(background, (0, 0))
		svin_anim.blit (adventure_screen, (200,300))
		self.block_group.draw (adventure_screen)
		start_screen.blit(font1.render (str(self.a), True, (250,250,250)),(0,0))


	def stage1_loop (self):

		self.a = timer.get_fps()

		if self.constructor == False:
			self.create_level (lev1)
			self.constructor = True

		self.render_stage1 ()
		timer.tick (30)
		pygame.display.flip()

		if self.k_space == True:
			self.stage1 = False
			self.stage2 = True

	def render_stage2 (self):

		adventure_screen.blit(background, (0, 0))

		self.block_group.draw (adventure_screen)
		start_screen.blit(font1.render (str(self.a), True, (250,250,250)),(0,0))


	def stage2_loop (self):

		self.a = timer.get_fps()

		if self.constructor2 == False:
			self.create_level (lev2)
			self.constructor2 = True

		self.render_stage2 ()
		timer.tick (30)
		pygame.display.flip() 



	def main_loop (self):

		self.render_main ()

		if self.stage1 == True:
			self.stage1_loop ()

		if self.stage2 == True:
			self.stage2_loop ()

		if self.stage3 == True:
			self.stage3_loop()

	def control_loop (self):

		while self.done:

			for e in pygame.event.get ():

				if e.type == pygame.QUIT:
					sys.exit ()

				if e.type == pygame.KEYDOWN:

					if e.key == pygame.K_SPACE:
						self.k_space = True

				if e.type == pygame.KEYUP:

					if e.key == pygame.K_SPACE:
						self.k_space = False

			self.main_loop ()


game = Main ()
game.control_loop ()



