
import pygame
import level1
import level2
import classes
import controller
import character
from level_data import *
from constants import *
import camera

level_width = len(lev1[0])*PF_WIDTH
level_height = len(lev1)*PF_HEIGHT

def camera_config (camera, target_rect):
		l = -target_rect.x + 810/2
		t = -target_rect.y + 420/2
		w,h = camera.width, camera.height

		l = min(0, l)                           # Не движемся дальше левой границы
		l = max(-(camera.width-810), l)   # Не движемся дальше правой границы
		t = max(-(camera.height-420), t) # Не движемся дальше нижней границы
		t = min(0, t)                           # Не движемся дальше верхней границы


		return pygame.Rect (l,t,w,h)

class main ():
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

camera = camera.Camera (camera_config, level_width, level_height)
control = controller.Holy_Spirit () 
view = classes.View_text (control)
hero = character.Hero (45,45, control, view)
stage1 = level1.Level(control, hero, lev1, camera)
stage2 = level2.Level(control, hero, lev2)
game = main (stage1, stage2, control)
game.main_loop ()



