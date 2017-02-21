
import pygame
#import random
import sys
#import pyganim
#from constants import *
#from classes import Platform
#from classes import Monster
#from functions import event_go
#from screens import *
from level1 import Level1
from level2 import Level2

class Control ():
	def __init__ (self):

		self.k_space = False
		self.stage1_flag = True
		self.stage2_flag = False
		self.flag = 0

	def control (self):
			for e in pygame.event.get ():

				if e.type == pygame.QUIT:
					sys.exit ()

				if e.type == pygame.KEYDOWN:

					if e.key == pygame.K_SPACE:
						self.k_space = True

				if e.type == pygame.KEYUP:

					if e.key == pygame.K_SPACE:
						self.k_space = False

class Main ():
	def __init__ (self, stage1, stage2, control):
		self.stage1 = stage1
		self.stage2 = stage2
		self.control = control

	def main_loop (self):

		while True:
			
			self.control.control ()

			if self.control.stage1_flag == True:
				if self.control.flag == 1:
					self.control.k_space = False
					self.control.flag = 0
				self.stage1.stage_loop ()

			if self.control.stage2_flag == True:
				if self.control.flag == 0:
					self.control.k_space = False
					self.control.flag = 1
				self.stage2.stage_loop ()
	
			pygame.display.flip()

		
control = Control ()
stage1 = Level1(control)
stage2 = Level2(control)
game = Main (stage1, stage2,control)

game.main_loop ()



