import pygame
import pyganim
import functions

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
		self.collide_control = False
		#self.etwas = nothing
		self.n = 0
		self.s = 1

	def conversation (self, tree):

		try:
			functions.render_text (tree[self.n])
		except:
			self.n = 0
			self.s = 1

		if self.control.k_1 == True:
			self.control.k_1 = False
			self.s = self.s*10
			self.n = (self.n+(1*self.s))
		if self.control.k_2 == True:
			self.control.k_2 = False
			self.s = self.s*10
			self.n = (self.n+(2*self.s))
		if self.control.k_3 == True:
			self.control.k_3 = False
			self.s = self.s*10
			self.n = (self.n+(3*self.s))

	def collide (self, array):

		for entity in array:
			if pygame.sprite.collide_rect (self, entity):
				return entity


	#def taking (self, array):

		#self.item = self.collide (array)
		#if self.collision == True:
			#self.collision = False
			#array.remove (self.item)

	def update (self, array):
		if self.collide_control == True:
			self.conversation(self.etwas.tree)


		#RIGHT
		if self.control.right == True:
			self.collide_control = False
			self.control.right = False

			self.rect.x += 1

			self.etwas = self.collide(array)

			if self.etwas != None:

				if self.etwas.name == "block":
					self.rect.x -= 1
					self.etwas.interaction ()
				if self.etwas.name == "chest":
					self.rect.x -= 1
					self.rect.x += 45
					array.remove (self.etwas)
				if self.etwas.name == "monster":
					self.rect.x -= 1
					self.collide_control = True
					self.etwas.interaction ()

			if self.etwas == None: 
				self.rect.x += 45
				self.rect.x -= 1
			
		#LEFT
		if self.control.left == True:
			self.control.left = False
			self.collide_control = False
			self.rect.x -= 1

			self.etwas = self.collide(array)
			if self.etwas != None:
				if self.etwas.name == "block" or self.etwas.name == "monster":
					self.rect.x += 1
					self.collide_control = True
					self.etwas.interaction ()
				if self.etwas.name == "chest":
					self.rect.x += 1
					self.rect.x -= 45
					array.remove (self.etwas)
				if self.etwas.name == "nothing":
					self.rect.x -= 45
					self.rect.x += 1
			if self.etwas == None: 
				self.rect.x -= 45
				self.rect.x += 1



		#UP
		if self.control.up == True:
			self.control.up = False
			self.collide_control = False
			self.rect.y -= 1

			self.etwas = self.collide(array)

			if self.etwas != None:

				if self.etwas.name == "block" or self.etwas.name == "monster":
					self.rect.y += 1
					self.collide_control = True
					self.etwas.interaction ()
				if self.etwas.name == "chest":
					self.rect.y += 1
					self.rect.y -= 45
					array.remove (self.etwas)
				if self.etwas.name == "nothing":
					self.rect.y -= 45
					self.rect.y += 1

			if self.etwas == None: 
				self.rect.y +=1
				self.rect.y -=45


		#DOWN
		if self.control.down == True:
			self.control.down = False
			self.collide_control = False
			self.rect.y += 1

			self.etwas = self.collide(array)
			if self.etwas != None:
				if self.etwas.name == "block" or self.etwas.name == "monster":
					self.rect.y -= 1
					self.collide_control = True
					self.etwas.interaction ()
				if self.etwas.name == "chest":
					self.rect.y -= 1
					self.rect.y += 45
					array.remove (self.etwas)
			if self.etwas == None: 
				self.rect.y += 45
				self.rect.y -= 1

		#self.etwas.interaction ()
		#if self.rect.x > 810:
		#	self.rect.x = 0
		#if self.rect.y > 450:
		#	self.rect.y = 0
		#if self.rect.x <0:
		#	self.rect.x = 810
		#if self.rect.y <0:
		#	self.rect.y = 450	

		pass
		#if self.collision == True:
		#	self.rect.x = 0
		#	self.rect.y = 0
		#	self.collision = False

	def render (self, surface):
		surface.blit(self.image, (self.rect.x, self.rect.y))
		#self.image.fill ((0,0,0))
		#svin_anim.blit (surface, (self.rect.x,self.rect.y))