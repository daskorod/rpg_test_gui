
import pygame
import sys
from level1 import Level1
from level2 import Level2
import classes
import controller
import character

class Father ():
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
	
			pygame.display.update()


control = controller.Holy_Spirit () 
hero = character.Hero (0,0, control)
stage1 = Level1(control, hero)
stage2 = Level2(control, hero)
game = Father (stage1, stage2, control)
game.main_loop ()



