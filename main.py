
import pygame
import random
import sys
import pyganim
from constants import *
from classes import Platform
from classes import Monster
from functions import event_go
from screens import *
from level1 import Level1


stage1 = Level1()



class Main ():
	def __init__ (self, stage1):

		self.x = 0
		self.y = 0
		self.stage1 = stage1
		self.done = True
		self.stage1 = True
		self.stage2 = False
		self.stage3 = False
		self.k_space = False
		#self.a = timer.get_fps()

	def stage_loop (self):

		self.render_main ()

	#	if self.stage1 == True:
		#	self.stage1_loop ()

		#if self.stage2 == True:
		#	self.stage2_loop ()

	#	if self.stage3 == True:
		#	self.stage3_loop()

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

			
			stage1.stage_loop ()

			pygame.display.flip()
			


game = Main (stage1)
game.control_loop ()



