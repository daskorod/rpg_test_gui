import pygame
class Monster ():
	def __init__ (self,att,ac,hp):
		self.att = att
		self.ac = ac
		self.hp = hp

class Printer ():
	def printing (self,a,b):
		print (a)
		print (b)

class Platform(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load ('images/wall.png')
		self.x = x
		self.y = y
		self.rect = self.image.get_rect ()
		self.rect.x = x
		self.rect.y = y

class Sprite(pygame.sprite.Sprite):
	"""docstring for Sprite"""
	def __init__(self, x, y, filename, att, ac, hp, mp):
		pygame.sprite.Sprite.__init__(self)

		self.image=pygame.image.load(filename)
		self.image.set_colorkey ((255,255,255))
		self.rect = pygame.Rect (0,0, 45,45)
		self.rect.x = x
		self.rect.y = y
		self.word = 'dwede'
		self.go_left = True
		self.xlocal = x
		self.ylocal = y
		self.xlocal_old = x
		self.ylocal_old = y
		self.att = att
		self.ac = ac
		self.hp = hp
		self.mp = mp
		self.xp = 0
		self.collide_monster = 0
		self.weapon = "Кор.меч"
		self.damage = 1
		self.hp_old = hp
		self.max_hp = hp


	def update (self, left, right, blocks, monsters):
		global minus, time_sec, time, stroke6, stopshow, stroke1,stroke2,stroke3,stroke4,stroke5,stroke7,stroke8,stroke9,stroke10,stroke13, stroke12, stroke12_red
		
		self.rect.x = self.xlocal
		self.rect.y = self.ylocal
		self.collide (blocks, monsters)
		stroke6 = 'Жизни: ' + str(hero.hp)

		
		self.xlocal_old = self.xlocal
		self.ylocal_old = self.ylocal

		stroke1 = 'Гидеон Рихтер'
		stroke2 = '     паладин'
		stroke3 = ' '
		stroke4 = 'Атака: '+ str(self.att)
		stroke5 = 'Защита: '+ str (self.ac)
		stroke6 = 'Жизни: ' + str(self.hp)
		stroke7 = ''
		stroke8 = 'Мана: ' + str (self.mp)
		stroke9 = 'Опыт: ' + str (self.xp)
		stroke10 = 'Зелья: ' + str(hppotionnum)
		stroke13 = str(self.weapon)+ ' урон: '+ str (self.damage)

		if self.hp > self.max_hp:
			self.hp = self.max_hp

		if self.hp_old >  self.hp:
			time_sec = 0
			time = 0
			stopshow = False
			minus = True
			stroke12_red = str(self.hp - self.hp_old) + " hp"
			
			self.hp_old = self.hp			
		if self.hp_old <  self.hp:
			time_sec = 0
			time = 0
			stopshow = False
			minus = False
			stroke12_red = "+ " + str(self.hp - self.hp_old) + " hp"
			
			self.hp_old = self.hp


	def collide (self, blocks, monsters):
		global collide_skelet, collide_zombi
		for pl in blocks:
			if pygame.sprite.collide_rect (self, pl):
				if self.xlocal < self.xlocal_old:
					
					
					self.xlocal = self.xlocal +45
				if self.xlocal > self.xlocal_old:
					
					
					self.xlocal = self.xlocal - 45
				if self.ylocal < self.ylocal_old:
					
					
					self.ylocal = self.ylocal +45
				if self.ylocal > self.ylocal_old:
					
					
					self.ylocal = self.ylocal - 45

		for element in monsters:
			if pygame.sprite.collide_rect (self, element) and element.dasein == 1:
				if self.xlocal < self.xlocal_old:
				
					self.xlocal = self.xlocal +45
					interaction_monster (element.name, element)
					if element.name == 'СКЕЛЕТ':
						collide_skelet = 1
					if element.name == 'ЗОМБИ':
						collide_zombi = 1

				if self.xlocal > self.xlocal_old:
									
					self.xlocal = self.xlocal - 45
					interaction_monster (element.name, element)
					collide_monster = 1
					if element.name == 'СКЕЛЕТ':
						collide_skelet = 1
					if element.name == 'ЗОМБИ':
						collide_zombi = 1
				if self.ylocal < self.ylocal_old:
							
					self.ylocal = self.ylocal +45
					interaction_monster (element.name, element)
					collide_monster = 1
					if element.name == 'СКЕЛЕТ':
						collide_skelet = 1
					if element.name == 'ЗОМБИ':
						collide_zombi = 1

				if self.ylocal > self.ylocal_old:
					self.ylocal = self.ylocal - 45
					interaction_monster (element.name, element)
					collide_monster = 1
					if element.name == 'СКЕЛЕТ':
						collide_skelet = 1
					if element.name == 'ЗОМБИ':
						collide_zombi = 1

		for element in items:
			if pygame.sprite.collide_rect (self, element):
				if self.xlocal < self.xlocal_old:
				
					
					interaction_item (element)
					items.remove (element)
					a_group.remove (element)
	

				if self.xlocal > self.xlocal_old:
									
					
					interaction_item (element)
					items.remove (element)
					a_group.remove (element)	
				if self.ylocal < self.ylocal_old:
							
					
					interaction_item (element)
					items.remove (element)
					a_group.remove (element)	

				if self.ylocal > self.ylocal_old:
					
					interaction_item (element)
					items.remove (element)
					a_group.remove (element)