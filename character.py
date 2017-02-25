import pygame
import pyganim

svin_anim_list = [('images/svin_motion.png',0.5),('images/svin_motion2.png',0.3),('images/svin_motion3.png',0.2)]
svin_anim = pyganim.PygAnimation(svin_anim_list)
svin_anim.play ()


class Hero(pygame.sprite.Sprite):

	def __init__(self, x, y, control):
		pygame.sprite.Sprite.__init__(self)

		#self.image=pygame.image.load(filename)
		#self.image.set_colorkey ((255,255,255))
		self.control = control
		self.image = pygame.Surface ((45,45))
		#self.image = svin_anim.getImagesFromSpriteSheet()
		self.image.fill ((100,200,230))
		self.rect = pygame.Rect (x,y, 45,45)
		self.rect.x = x
		self.rect.y = y
		self.collision = False
		self.block_group = []
		self.item = []

	def collide (self, array):

		for entity in array:
			if pygame.sprite.collide_rect (self, entity):
				self.collision = True
				return entity

	def taking (self, array):

		self.item = self.collide (array)
		if self.collision == True:
			self.collision = False
			array.remove (self.item)

	def update (self, blocks):

		if self.control.right == True:
			self.control.right = False
			self.rect.x += 1
			self.collide (blocks)
			if self.collision == False:
				self.rect.x += 45
				self.rect.x -= 1
			if self.collision == True:
				self.rect.x -= 1
			self.collision = False

		if self.control.left == True:
			self.control.left = False
			self.rect.x -= 1
			self.collide (blocks)
			if self.collision == False:
				self.rect.x -= 45
				self.rect.x += 1
			if self.collision == True:
				self.rect.x += 1
			self.collision = False

		if self.control.up == True:
			self.control.up = False
			self.rect.y -= 1
			self.collide (blocks)
			if self.collision == False:
				self.rect.y -= 45
				self.rect.y += 1
			if self.collision == True:
				self.rect.y += 1
			self.collision = False	

		if self.control.down == True:
			self.control.down = False
			self.rect.y += 1
			self.collide (blocks)
			if self.collision == False:
				self.rect.y += 45
				self.rect.y -= 1
			if self.collision == True:
				self.rect.y -= 1
			self.collision = False

		if self.rect.x > 810:
			self.rect.x = 0
		if self.rect.y > 450:
			self.rect.y = 0
		if self.rect.x <0:
			self.rect.x = 810
		if self.rect.y <0:
			self.rect.y = 450	

		pass
		#if self.collision == True:
		#	self.rect.x = 0
		#	self.rect.y = 0
		#	self.collision = False

	def render (self, surface):
		surface.blit(self.image, (self.rect.x, self.rect.y))
		#self.image.fill ((0,0,0))
		#svin_anim.blit (surface, (self.rect.x,self.rect.y))