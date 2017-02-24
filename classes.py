from pygame import sprite
from pygame import image
from pygame import Rect
from pygame import Surface

#import pygame
#Classes

class Monster(sprite.Sprite):
	def __init__(self, x, y, filename):
		sprite.Sprite.__init__(self)
		self.image=image.load(filename)
		self.image.set_colorkey ((255,255,255))
		self.rect = Rect (0,0, 45,45)
		self.rect.x = x
		self.rect.y = y

class Platform(sprite.Sprite):
	def __init__(self, x, y):
		sprite.Sprite.__init__(self)
		#self.image=image.load(filename)
		#self.image.set_colorkey ((255,255,255))
		self.image = Surface ((45,45))
		self.image.fill ((100,100,100))
		self.rect = Rect (0,0, 45,45)
		self.rect.x = x
		self.rect.y = y

class Hero(sprite.Sprite):
	"""docstring for Sprite"""
	def __init__(self, x, y, control):
		sprite.Sprite.__init__(self)

		#self.image=pygame.image.load(filename)
		#self.image.set_colorkey ((255,255,255))
		self.control = control
		self.image = Surface ((45,45))
		self.image.fill ((100,100,100))
		self.rect = Rect (x,y, 45,45)
		self.rect.x = x
		self.rect.y = y


	def update (self):
		if self.control.right == True:
			self.control.right = False
			self.rect.x += 45
		if self.control.left == True:
			self.control.left = False
			self.rect.x -= 45
		if self.control.up == True:
			self.control.up = False
			self.rect.y -= 45
		if self.control.down == True:
			self.control.down = False
			self.rect.y += 45			
		pass



	def collide (self):
		pass

	def render (self, surface):
		surface.blit(self.image, (self.rect.x, self.rect.y))
