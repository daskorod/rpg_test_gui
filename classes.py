from pygame import sprite
from pygame import image
from pygame import Rect
from pygame import Surface
import pyganim
import screens
import fonts
import functions
import text
from screens import *

class View_text ():
	def __init__ (self, control):
		self.a_max = 0
		self.n = 0
		self.a = 0
		self.control = control

	def render_text (self,text):

		self.a_max = len(text)//350
		self.n = self.a*350

		if self.control.k_n == True:
			self.control.k_n = False
			self.s1 = text[self.n+0:self.n+50]
			if self.a < self.a_max:
				self.a = self.a+1
			else:
				self.a = 0

		s1 = text[self.n+0:self.n+50]
		s2 = text[self.n+50:self.n+100]
		s3 = text[self.n+100:self.n+150]
		s4 = text[self.n+150:self.n+200]
		s5 = text[self.n+200:self.n+250]
		s6 = text[self.n+250:self.n+300]
		s7 = text[self.n+300:self.n+350]
	
		information_screen.blit(fonts.font2.render (str(s1), True, (250,250,250)),(2,0))
		information_screen.blit(fonts.font2.render (str(s2), True, (250,250,250)),(2,22))
		information_screen.blit(fonts.font2.render (str(s3), True, (250,250,250)),(2,44))
		information_screen.blit(fonts.font2.render (str(s4), True, (250,250,250)),(2,66))
		information_screen.blit(fonts.font2.render (str(s5), True, (250,250,250)),(2,88))
		information_screen.blit(fonts.font2.render (str(s6), True, (250,250,250)),(2,110))
		information_screen.blit(fonts.font2.render (str(s7), True, (250,250,250)),(2,132))	


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
