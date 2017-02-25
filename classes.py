from pygame import sprite
from pygame import image
from pygame import Rect
from pygame import Surface
import pyganim

#import pygame
#Classes


		#adventure_screen.blit(background, (0, 0))
		#svin_anim.blit (adventure_screen, (200,300))
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

class Chest(sprite.Sprite):
	def __init__(self, x, y):
		sprite.Sprite.__init__(self)
		#self.image=image.load(filename)
		#self.image.set_colorkey ((255,255,255))
		self.image = Surface ((45,45))
		self.image.fill ((200,30,70))
		self.rect = Rect (0,0, 45,45)
		self.rect.x = x
		self.rect.y = y