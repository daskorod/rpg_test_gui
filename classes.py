from pygame import sprite
from pygame import image
from pygame import Rect
from pygame import Surface
import pyganim
import screens
import fonts
import functions
import text



#import pygame
#Classes


		#adventure_screen.blit(background, (0, 0))
		#svin_anim.blit (adventure_screen, (200,300))
class Monster(sprite.Sprite):
	def __init__(self, x, y, textus):
		sprite.Sprite.__init__(self)
		#self.image=image.load(filename)
		#self.image.set_colorkey ((255,255,255))
		self.image = Surface ((45,45))
		self.image.fill ((120,30,200))
		self.a = "Я злобный монстр!"
		self.rect = Rect (0,0, 45,45)
		self.rect.x = x
		self.rect.y = y
		self.name = "monster"
		self.textus = text
		self.n = 0
		self.s = 1
		self.tree = text.zombi1

	#def conversation (self):
		#hero.conversation (text.zombi1)

	def interaction (self):
		#screens.information_screen.blit(fonts.font1.render ((self.a), True, (250,250,250)),(0,0))
		#self.conversation ()
		pass




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
		self.name = "block"
	def interaction (self):
		pass

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
		self.name = "chest"
	def interaction (self):
		pass
