from pygame import Surface
from functions import create_level
from screens import *

class Level ():

	def __init__ (self, control):
	#	self.lev = lev
	#    self.platforms, self.block_group = create_level (self.lev)
	  #  self.control = control

	def render_interface (self):

		window.blit(start_screen, (10, 10))
		start_screen.fill ((black))
		start_screen.blit (adventure_screen, (0,0))
		start_screen.blit (instrumental_screen, (0,450))
		instrumental_screen.blit (hero_screen, (0,0))
		hero_screen.fill ((cool_orange))
		instrumental_screen.blit (information_screen, (150,0))
		information_screen.fill ((50,50,50))
		instrumental_screen.blit (monster_screen, (650,0))
		monster_screen.fill ((sea_color))
