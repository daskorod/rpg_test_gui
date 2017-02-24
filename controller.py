import pygame
import sys




class Control ():
	def __init__ (self):

		self.k_space = False
		self.stage1_flag = True
		self.stage2_flag = False
		self.flag = 0
		self.left = False
		self.right = False
		self.up = False
		self.down = False
		

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

				if e.type == pygame.KEYDOWN:
					if e.key == pygame.K_LEFT:
						self.left = True

					if e.key == pygame.K_RIGHT:
						self.right = True

				if e.type == pygame.KEYDOWN:
					if e.key == pygame.K_UP:
						self.up = True

					if e.key == pygame.K_DOWN:
						self.down = True

				if e.type == pygame.KEYUP:
					if e.key == pygame.K_LEFT:
						self.left = False

					if e.key == pygame.K_RIGHT:
						self.right = False

				if e.type == pygame.KEYUP:
					if e.key == pygame.K_UP:
						self.up = False

					if e.key == pygame.K_DOWN:
						self.down = False
